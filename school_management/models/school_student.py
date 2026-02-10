# -*- coding: utf-8 -*-
import xlsxwriter
import base64
from io import BytesIO
from datetime import date

from odoo import models, fields, api, Command
from odoo.exceptions import ValidationError, UserError
from odoo.http import request


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student record'
    _order = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    student_id = fields.Char(string='Student ID')
    name = fields.Char(string='Name', required=True)
    roll_no = fields.Char(string='Roll No.')
    dob = fields.Date(string='Date of Birth')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    fees_status = fields.Selection([('paid', 'Paid'), ('unpaid', 'Unpaid')], string='Fees Status', default='unpaid')
    total_fee = fields.Float(string='Total fee', compute='_compute_fees', store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string='Gender')
    class_id = fields.Many2one('school.class', string='Class', ondelete='cascade',
                               domain=lambda self: self._get_class_domain())
    subject_ids = fields.Many2many('school.subject', string='Subject')
    total_subjects = fields.Integer(string='Total subjects', compute="_compute_total_subjects", store=True)
    status = fields.Selection([('minor', 'Minor'), ('adult', 'Adult')], string='Status', compute="_compute_status",
                              store=True)
    user_id = fields.Many2one('res.users', string='User')
    email = fields.Char(string='Email', required=True, unique=True)
    exam_given = fields.Boolean(string='Exam Given', compute='_compute_exam_given')
    exam_ids = fields.One2many('school.exam', 'student_id', string='Exams')
    display_name = fields.Char(string='Display Name', compute='_compute_display_name')
    student_count = fields.Integer(compute='_compute_student_count', store=True)

    @api.depends('subject_ids')
    def _compute_total_subjects(self):
        for record in self:
            record.total_subjects = len(record.subject_ids)

    @api.depends('class_id')
    def _compute_fees(self):
        for record in self:
            if record.class_id and record.class_id.name and int(record.class_id.name) <= 5:
                record.total_fee = 10000
            else:
                record.total_fee = 20000

    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.dob:
                record.age = today.year - record.dob.year
            else:
                record.age = 0

    @api.onchange('class_id')
    def _onchange_class_id(self):
        if (self.class_id):
            self.subject_ids = [(6, 0, self.class_id.subject_ids.ids)]
        else:
            self.subject_ids = [(5, 0, 0)]

    @api.depends('age')
    def _compute_status(self):
        for record in self:
            record.status = 'minor' if record.age < 18 else 'adult'

    @api.constrains('subject_ids')
    def _check_subject_limit(self):
        for record in self:
            if len(record.subject_ids) > 6:
                raise ValidationError('Subject limit exceeded (max 6)!')

    def view_subjects(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Subjects',
            'res_model': 'school.subject',
            'view_mode': 'list,form',
            'domain': [('id', 'in', self.subject_ids.ids)]
        }

    def action_view_exams(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Exams',
            'res_model': 'school.exam',
            'view_mode': 'list,form',
            'domain': [('student_id', '=', self.id)],
            'context': {'default_student_id': self.id}
        }

    @api.model_create_multi
    def create(self, vals_list):
        students = super().create(vals_list)
        user = self.env['res.users'].sudo().create({
            'name': students.name,
            'login': students.email,
            'password': 'student123',
            'groups_id': [
                Command.link(self.env.ref('school_management.group_student').id)
            ],
        })
        students.user_id = user.id

        for student in students:
            if student.class_id:
                roll = self.env['ir.sequence'].sudo().next_by_code('school.student')
                student.roll_no = roll.replace('STD', str(student.class_id.name))
            else:
                student.roll_no = False

        return students

    @api.constrains('class_id', 'roll_no')
    def _check_roll_no_unique(self):
        for student in self:
            if student.roll_no:
                duplicate = self.search([
                    ('class_id', '=', student.class_id.id),
                    ('roll_no', '=', student.roll_no),
                    ('id', '!=', student.id)
                ])
                if duplicate:
                    raise ValidationError(
                        "Roll No is already assigned to another student in class!"
                    )

    def _get_class_domain(self):
        if self.env.user.has_group('school_management.group_teacher'):
            return [('teacher_id', '=', self.env.user.id)]

    def _compute_exam_given(self):
        for record in self:
            count = self.env['school.exam'].search_count([
                ('student_id', '=', record.id)
            ])
            record.exam_given = True if count > 0 else False

    @api.depends('name', 'class_id', 'roll_no')
    def _compute_display_name_full(self):
        for student in self:
            if student.class_id and student.roll_no:
                student.display_name_full = f"{student.name}-{student.class_id.name}-{student.roll_no}"
            else:
                student.display_name_full = f"{student.name}-{student.roll_no}"

    def _compute_display_name(self):
        for record in self:
            if self.env.context.get('exam_dropdown'):
                record.display_name = f"{record.name}-{record.class_id.name}-{record.roll_no}"
            else:
                record.display_name = f"{record.name}"

    def action_download_excel(self):
        student_ids = self.ids
        ids_str = ",".join(str(i) for i in student_ids)
        url = f'/student/excel?ids={ids_str}'
        return {
            'type': 'ir.actions.act_url',
            'url': url,
            'target': 'self',
        }

    def check_fees_due_reminder(self):
        students = self.search([
            ('fees_status', '=', 'unpaid'),
        ])
        for student in students:
            student.message_post(body="Fees is still due.Kindly pay as earliest as possible", subject="Fees Reminder")

    def _compute_student_count(self):
        for record in self:
            record.student_count = 1

