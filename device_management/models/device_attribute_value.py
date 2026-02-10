# -*- coding: utf-8 -*-
from odoo import models, fields, api


class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'
    _description = 'Device Attribute Value'

    device_attribute_value_name = fields.Char(required=True)
    device_attribute_id = fields.Many2one('device.attribute')