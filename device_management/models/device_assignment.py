# -*- coding: utf-8 -*-
from odoo import models,fields, api


class DeviceAssignment(models.Model):
    _name = 'device.assignment'
    _description = 'Device Assignment'

    name = fields.Char(string='Name')
    device_manage_id = fields.Many2one(comodel_name='device.manage',string='Device Id')
    employee_id = fields.Many2one(comodel_name='hr.employee',string='Employee Id')
    date_start = fields.Date(string='Start Date')
    date_expire = fields.Date(string='Expire Date')
    state = fields.Selection([('new','New'),('draft','Draft'),('approved','Approved'),('rejected','Rejected')],string='State')
