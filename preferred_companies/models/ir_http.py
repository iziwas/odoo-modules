from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    def session_info(self):
        """ Override to add preferred_companies in session_info method """
        result = super(IrHttp, self).session_info()
        
        result["user_companies"].update({
            "preferred_companies": self.env.user.preferred_company_ids.ids
        })
        
        return result