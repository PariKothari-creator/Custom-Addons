# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'
    _description = 'Device Attribute Assignment'

    device_manage_id = fields.Many2one(comodel_name='device.manage')
    device_attribute_id = fields.Many2one(comodel_name='device.attribute')
    device_attribute_value_id = fields.Many2one(comodel_name='device.attribute.value')


