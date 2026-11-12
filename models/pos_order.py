from odoo import models

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def _prepare_invoice_vals(self):
        res = super(PosOrder, self)._prepare_invoice_vals()
        
        
        if self.partner_id and self.partner_id.user_id:

            res['invoice_user_id'] = self.partner_id.user_id.id
            
        return res