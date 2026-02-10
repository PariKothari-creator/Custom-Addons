# -*- coding: utf-8 -*-
from odoo import models,fields,api


class SaleOrderLineExtension(models.Model):
    _inherit = 'sale.order.line'

    additional_qty = fields.Integer(string="Additional Quantity", default=0.0)
    final_amount = fields.Float(string="Final Amount", compute="_compute_additional_final_amount", store=True)

    @api.depends('additional_qty', 'price_unit', 'product_uom_qty')
    def _compute_additional_final_amount(self):
        for line in self:
            base_extra = line.additional_qty * line.price_unit

            line.final_amount = base_extra * line.product_uom_qty

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _cart_update(self, product_id=None, line_id=None, add_qty=0, set_qty=0, **kwargs):
        res = super(SaleOrder, self)._cart_update(product_id, line_id, add_qty, set_qty, **kwargs)

        if res.get('line_id'):
            line = self.env['sale.order.line'].browse(res['line_id'])

            add_qty_val = int(kwargs.get('additional_qty', 0))

            if add_qty_val > 0:
                line.write({
                    'additional_qty': add_qty_val,
                })

        return res

class CustomSaleOrderLine(models.Model):
    _inherit = 'custom.sale.order.line'

    additional_qty = fields.Float(string="Additional Quantity", default=0.0, store=True)



































