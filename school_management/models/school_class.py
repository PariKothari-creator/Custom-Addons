# -*- coding: utf-8 -*-
from odoo import models,fields,api


class SchoolClass(models.Model):
    _name="school.class"
    _description = "School Class"
    _order = "name"

    name = fields.Integer(string = 'Class Name',required=True)
    teacher_id = fields.Many2one('res.users',string='Class Teacher',domain=lambda self: [
        ('groups_id', 'in',
         self.env.ref('school_management.group_teacher').id)
    ],ondelete='set null')
    subject_ids=fields.Many2many('school.subject',string='Subjects',ondelete='cascade')
    advisor = fields.Reference(selection=[('res.partner','Parent/Guardian'),('res.users','Teacher')],string='Advisor')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

