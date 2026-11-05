from odoo.exceptions import AccessError, ValidationError
from odoo.tests.common import Form, TransactionCase, new_test_user, tagged


@tagged("post_install", "-at_install")
class TestPreferredCompanies(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.company_main = cls.env.company
        cls.company_allowed = cls.env["res.company"].create({"name": "Allowed"})
        cls.company_forbidden = cls.env["res.company"].create({"name": "Forbidden"})
        allowed = cls.company_main + cls.company_allowed
        cls.user = new_test_user(
            cls.env,
            login="preferred_user",
            groups="base.group_user",
            company_id=cls.company_main.id,
            company_ids=[(6, 0, allowed.ids)],
            tz="Europe/Paris",
        )
        cls.other_user = new_test_user(
            cls.env,
            login="preferred_other_user",
            groups="base.group_user",
            company_id=cls.company_main.id,
            company_ids=[(6, 0, allowed.ids)],
        )

    def test_user_sets_own_preferences_from_form(self):
        """A non-admin user can save the field from their preferences form."""
        form = Form(
            self.user.with_user(self.user),
            view="base.view_users_form_simple_modif",
        )
        form.preferred_company_ids.add(self.company_allowed)
        form.save()
        self.assertEqual(self.user.preferred_company_ids, self.company_allowed)

    def test_user_cannot_select_forbidden_company(self):
        with self.assertRaises(ValidationError):
            self.user.with_user(self.user).write(
                {"preferred_company_ids": [(6, 0, self.company_forbidden.ids)]}
            )

    def test_user_cannot_edit_other_user(self):
        with self.assertRaises(AccessError):
            self.other_user.with_user(self.user).write(
                {"preferred_company_ids": [(6, 0, self.company_allowed.ids)]}
            )

    def test_revoked_company_is_removed_from_preferences(self):
        self.user.preferred_company_ids = self.company_allowed
        self.user.company_ids -= self.company_allowed
        self.assertFalse(self.user.preferred_company_ids)
