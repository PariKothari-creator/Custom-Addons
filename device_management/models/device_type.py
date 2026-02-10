# -*- coding: utf-8 -*-
from odoo import models, fields, api


class DeviceType(models.Model):
    _name = 'device_type'
    _description = 'Device Type'
    _sql_constraints = [('unique_name', 'unique(name)', 'The Device name must be unique'),('unique-code','unique(code)', 'The Device code must be unique')]

    device_type_name = fields.Char(string='Device Type', required=True)
    code =  fields.Char(string='Device Code', required=True)
    sequence = fields.Char(string='Sequence',default=lambda self: self.env['ir.sequence'].next_by_code('device_type'))
    device_attribute_ids = fields.Many2many(comodel_name='device.attribute', string='Device Attributes')
    device_model_ids = fields.Many2many(comodel_name='device.model', string='Device Models')
    device_ids = fields.Many2many(comodel_name='device', string='Devices')

