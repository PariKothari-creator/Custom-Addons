# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleExtension(models.Model):
    _inherit = 'sale.order'

    customer_phone = fields.Char(string="Customer Phone")
    custom_order_line_ids = fields.One2many('custom.sale.order.line', 'order_id')


    def action_customize_order_line(self):
        return {
            'name': 'Customize Order Line',
            'type': 'ir.actions.act_window',
            'res_model': 'custom.order.line.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'active_id': self.id, 'default_order_id': self.id},
        }

    def _create_invoices(self, final=False, grouped=False):
        invoices = super()._create_invoices(final=final, grouped=grouped)
        for order in self:
            if order.custom_order_line_ids:
                for inv in invoices:
                    for line in order.custom_order_line_ids:
                        self.env['custom.invoice'].create({
                            'invoice_id': inv.id,
                            'product_id': line.product_id.id,
                            'quantity': line.quantity,
                            'taxes': line.taxes,
                            'price_unit': line.price_unit,
                            'amount': line.amount,
                        })
        return invoices
