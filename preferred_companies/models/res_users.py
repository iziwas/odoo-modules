from odoo import models, fields


class ResUsers(models.Model):
    _inherit = "res.users"

    preferred_company_ids = fields.Many2many(
        "res.company",
        "user_id",
        string="Preferred companies"
    )

    def _get_preferred_companies(self):
        return self.preferred_company_ids.ids