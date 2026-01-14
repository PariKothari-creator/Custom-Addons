# -*- coding: utf-8 -*-
from odoo import models,fields,api


class CustomOrderLine(models.Model):
    _name = "custom.sale.order.line"
    # _description = "Custom Order Line"

    order_id = fields.Many2one('sale.order',string="Sale Order",required=True,ondelete='cascade')
    product_id = fields.Many2one('product.product',string="Product",required=True)
    quantity = fields.Integer(string="Quantity")
    price_unit = fields.Float(string="Unit Price")
    taxes = fields.Many2many('account.tax',string='Taxes')
    amount = fields.Float(string="Amount", compute='_compute_amount')
    sale_line_id = fields.Many2one('sale.order.line',string="Sale Line", ondelete='cascade')

    @api.depends('quantity', 'price_unit')
    def _compute_amount(self):
        for line in self:
            line.amount = line.price_unit * line.quantity
