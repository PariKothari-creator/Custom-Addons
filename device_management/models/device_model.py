# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DeviceModel(models.Model):
    _name = 'device.model'
    _description = 'Device Model'
    _sql_constraints = [('name_unique', 'unique(device_model_name)', 'Device Model')]

    device_model_name = fields.Char(string= 'Device Model' ,required=True)
    device_type_id = fields.Many2one(comodel_name='device.type', string='Device Type')
    device_brand_id = fields.Many2one(comodel_name='brand.device', string='Device Brand')
