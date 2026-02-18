# -*- coding: utf-8 -*-
from odoo import models,fields,api
from datetime import date
from odoo.exceptions import ValidationError

class SchoolExam(models.Model):
    _name='school.exam'
    _description = 'Student Exam Record'

    name=fields.Selection([('mid','Mid Sem'),('end','End Sem'),('quiz','Quiz')], string="Exam Type",required=True)
    exam_date=fields.Date(string="Date of Conduct",required=True)
    image_1920=fields.Image(string="Invigilator Sign")
    student_id=fields.Many2one('school.student',string="Students", context={'exam_dropdown':True})
    class_id=fields.Many2one('school.class',string="Class" ,store=True,readonly=True,related='student_id.class_id')
    exam_subjects_ids=fields.One2many('exam.subjects','exam_id',string="Exam Subjects")
    total_marks=fields.Integer(string="Total Marks",compute='_compute_total_marks',store=True)
    avg_marks=fields.Integer(string="Average Marks",compute='_compute_avg_marks',store=True)
    result=fields.Selection([('pass','Pass'),('fail','Fail')],string="Result")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)
    widget_placeholder = fields.Integer(string="Progress", default=0)

    @api.depends('exam_subjects_ids.marks')
    def _compute_avg_marks(self):
        for record in self:
            total=0
            count=0
            for line in record.exam_subjects_ids:
                if line.marks is not None:
                    total +=line.marks
                    count+=1
            record.avg_marks = total/count if count else 0

    @api.depends('exam_subjects_ids.marks')
    def _compute_total_marks(self):
        for record in self:
            total = 0
            for line in record.exam_subjects_ids:
                if line.marks:
                    total += line.marks
            record.total_marks = total

    @api.onchange('total_marks')
    def _onchange_result(self):
        for record in self:
            if record.total_marks >150:
                record.result = 'pass'
            else:
                record.result = 'fail'

    def write(self,vals):
        if 'total_marks' in vals:
            vals['result'] = 'pass'if vals['total_marks'] > 150 else 'fail'
        return super(SchoolExam,self).write(vals)

    @api.onchange('class_id')
    def _onchange_class(self):
        if self.class_id:
            self.exam_subjects_ids = [(5,0,0)]
            for record in self.class_id.subject_ids:
                self.exam_subjects_ids=[(0,0,{'subject_id' : record.id, 'marks':0})]
