# -*- conding: utf-8 -*-
from odoo import models,fields,api
from zeep.exceptions import ValidationError


class ExamSubjects(models.Model):
    _name='exam.subjects'
    _description='Exam Subjects With Marks'

    exam_id=fields.Many2one(comodel_name='school.exam',string='Exam Name' ,ondelete='cascade')
    student_id=fields.Many2one(comodel_name='school.student',string='Student Name', required=True)
    subject_id=fields.Many2one('school.subject',string='Subject Name',required=True)
    class_id=fields.Many2one('school.class',string='Class',required=True, store=True)
    marks=fields.Float(string='Marks',required=True)
    max_marks=fields.Integer(string='Max Marks',required=True,default=100)

    @api.constrains('max_marks')
    def _check_max_marks(self):
        for record in self:
            if record.marks > record.max_marks:
                raise ValidationError('Marks cannot be more than 100')


