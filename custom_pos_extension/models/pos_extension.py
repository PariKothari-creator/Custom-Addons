from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    description_pos = fields.Text(string="POS Description")


class ProductProduct(models.Model):
    _name = 'product.product'
    _inherit = 'product.product'
    #
    # description_pos = fields.Text(
    #     related="product_tmpl_id.description_pos",
    #     store=True,
    # )

    @api.model
    def _load_pos_data_fields(self, config_id):
        fields = super()._load_pos_data_fields(config_id)
        fields += ['description_pos']
        return fields


