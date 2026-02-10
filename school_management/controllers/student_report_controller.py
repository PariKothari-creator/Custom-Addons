from odoo import models, fields
from odoo import http
from odoo.http import request
from io import BytesIO
from odoo.exceptions import UserError
import base64
import xlsxwriter

class StudentReportController(http.Controller):
    @http.route('/student/excel', type='http', auth='user')
    def download_student_excel(self, **kw):
      active_ids = request.params.get('ids')
      student_ids = [int(x) for x in active_ids.split(',')]
      students = request.env['school.student'].browse(student_ids)
      filename = "student.xlsx"
      output = BytesIO()
      workbook = xlsxwriter.Workbook(output)
      sheet1 = workbook.add_worksheet('Students')

      headers = ['Name', 'Roll No', 'Class', 'Gender', 'Age', 'Total Subjects']
      for col, head in enumerate(headers):
          sheet1.write(0, col, head)

      row = 1
      for student in students:
          sheet1.write(row, 0, student.name)
          sheet1.write(row, 1, student.roll_no)
          sheet1.write(row, 2, student.class_id.name)
          sheet1.write(row, 3, student.gender)
          sheet1.write(row, 4, student.age)
          sheet1.write(row, 5, student.total_subjects)

          row += 1
      workbook.close()
      output.seek(0)

      return request.make_response(output.getvalue(),
                                   headers=[
                                       ('Content-Type',
                                        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                                       ('Content-disposition', 'attachment; filename=student.xlsx;')])

