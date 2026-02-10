# -*- coding: utf-8 -*-

from odoo import models,fields,api

class StudentsFeedback(models.Model):
    _name = 'students.feedback'
    _description = 'Student Feedback'

    student_id = fields.Many2one('school.student',string='Student',required=True)
    teacher_id = fields.Many2one('res.users',string='Teacher',required=True)
    rating = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5')],string='Rating')
    remarks = fields.Text(string='Remarks')
    class_id = fields.Many2one('school.class',string='Class',required=True)
    feedback_date = fields.Datetime(string='Date',required=True)
    discipline_grade = fields.Char(string='Discipline Grade')
