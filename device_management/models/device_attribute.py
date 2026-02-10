# -*- coding: utf-8 -*-
from odoo import models, fields, api


class DeviceAttribute(models.Model):
    _name = 'device.attribute'
    _description = 'Device Attribute'

    device_attribute_name = fields.Char(string='Name')
    device_type_id = fields.Many2one(comodel_name='device.type')
    required = fields.Boolean(default=True)
    device_attribute_value_ids = fields.Many2many(comodel_name='device.attribute.value')