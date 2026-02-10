# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Employee(models.Model):
    _inherit = 'hr.employee'

    device_assignment_ids = fields.Many2many(comodel_name='device.assignment',string='Device Assignment')