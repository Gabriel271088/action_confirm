from odoo import models, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

      def action_confirm(self):
        res = super().action_confirm()
        
        if invoices:
            invoices.sudo().action_confirm()
            self.sudo().run_invoicing_atomation()
            if self.type_id.set_done_on_confirmation:
                self.action_confirm()
        return res