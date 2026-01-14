from odoo import models,fields,api


class CustomOrderLineWizardLine(models.TransientModel):
    _name = 'custom.order.line.wizard.line'
    _description = 'Custom Order Line Wizard Line'
    _rec_name = 'product_id'

    wizard_id = fields.Many2one('custom.order.line.wizard',string="Wizard Line")

    product_id = fields.Many2one('product.product', string="Product", required=True)

    quantity = fields.Integer(string="Quantity")

    price_unit = fields.Float(string="Unit Price")

    taxes = fields.Many2many('account.tax', string="Taxes", readonly=False)

    amount = fields.Float(string="Amount", compute="_compute_amount")

    custom_line_id = fields.Many2one('custom.sale.order.line', string="Custom Line")

    @api.depends('quantity', 'price_unit')
    def _compute_amount(self):
        for line in self:
            line.amount = line.price_unit * line.quantity


