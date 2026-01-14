# -*- coding: utf-8 -*-
from odoo import models,fields,api


class CustomInvoice(models.Model):
    _name = 'custom.invoice'
    _description = 'Customer Invoice'

    invoice_id = fields.Many2one('account.move', string="Account Move", required=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', string="Product", required=True)
    quantity = fields.Float(string="Quantity")
    price_unit = fields.Float(string="Unit Price")
    taxes = fields.Many2many('account.tax', string='Taxes')
    amount = fields.Float(string="Amount")

    @api.depends('quantity', 'price_unit')
    def _compute_amount(self):
        for line in self:
            line.amount = line.price_unit * line.quantity





