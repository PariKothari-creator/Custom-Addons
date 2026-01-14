from odoo import models, fields, api


class CustomOrderLineWizard(models.TransientModel):
    _name = 'custom.order.line.wizard'
    _description = 'Custom Order Line Wizard'

    order_id = fields.Many2one('sale.order', string="Sale Order", required=True, ondelete='cascade')

    line_ids = fields.One2many('custom.order.line.wizard.line', 'wizard_id')

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        active_id = self.env.context.get('active_id')
        if active_id:
            sale_order = self.env['sale.order'].browse(active_id)
            res['order_id'] = sale_order.id

            lines_command = []
            for line in sale_order.order_line:
                lines_command.append((0, 0, {
                    'product_id': line.product_id.id,
                    'quantity': line.product_uom_qty,
                    'price_unit': line.price_unit,
                    'taxes': line.tax_id.ids,
                    'amount': line.price_subtotal
                }))
            res['line_ids'] = lines_command
        return res

    def action_save(self):
        wizard_data = []
        for line in self.line_ids:
            wizard_data.append({
                'product_id': line.product_id.id,
                'quantity': line.quantity,
                'price_unit': line.price_unit,
                'taxes': line.taxes.ids,
                'amount': line.amount
            })
        self.env['custom.sale.order.line'].search([]).unlink()

        for vals in wizard_data:
            self.env['custom.sale.order.line'].create({
                'product_id': vals['product_id'],
                'quantity': vals['quantity'],
                'price_unit': vals['price_unit'],
                'taxes': [(6, 0, vals['taxes'])],
                'amount': vals['amount'],
            })
        self.line_ids.unlink()
