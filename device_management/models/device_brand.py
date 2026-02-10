# -*- coding: utf-8 -*-
from odoo import models, fields, api


class device_brand(models.Model):
    _name = 'device.brand'
    _description = 'device brand'
    _sql_constraints = [('name_unique', 'unique', 'Device Brand must be unique')]


    device_brand_name = fields.Char(string='Name')
    device_model_id = fields.Many2one(comodel_name='device.model', string='Device Models')