from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResUsers(models.Model):
    _inherit = "res.users"

    preferred_company_ids = fields.Many2many(
        "res.company",
        "res_users_preferred_company_rel",
        "user_id",
        "company_id",
        string="Preferred companies",
    )

    def _get_preferred_companies(self):
        return self.preferred_company_ids.ids

    @api.constrains("preferred_company_ids")
    def _check_preferred_companies(self):
        for user in self:
            if user.preferred_company_ids - user.company_ids:
                raise ValidationError(
                    _("Preferred companies must be among the user's allowed companies.")
                )

    def write(self, vals):
        result = super().write(vals)
        if "company_ids" in vals:
            for user in self:
                stale = user.preferred_company_ids - user.company_ids
                if stale:
                    user.preferred_company_ids -= stale
        return result
