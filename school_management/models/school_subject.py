# -*- coding: utf-8 -*-

from odoo import models,fields,api


class SchoolSubject(models.Model):
    _name ='school.subject'
    _description ='School Subject'

    name = fields.Char(string= 'Name', help='Name of the subject',required=True)
    code = fields.Char(string = 'Subject Code')
    teacher_id = fields.Many2one('res.users',string=' Subject Teacher', ondelete='cascade')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
