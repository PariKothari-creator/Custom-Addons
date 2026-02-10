{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Manages Students Records',
    'description': 'Compelete record of school management',
    'depends': ['base', 'hr', 'sale'],
    'data': [
        'security/school_security.xml',
        'security/ir.model.access.csv',
        'views/res_config_setting_view.xml',
        'views/school_subject_view.xml',
        'views/school_class_view.xml',
        'views/school_student_view.xml',
        'data/ir_sequence_student.xml',
        'data/ir.cron_check_fees_status.xml',
        'views/school_exam_view.xml',
        'views/exam_subjects.xml',
        'views/students_feedback_views.xml',
        'views/student_menu_view.xml',
        'reports/student_reports.xml',
        'reports/student_reports_template.xml',

    ],
    'assets': {
        'web.assets_backend': [
            'school_management/static/src/js/student_feedback.js',
            'school_management/static/src/xml/student_feedback.xml',
            'school_management/static/src/scss/feedback_stars.scss'
        ]
    },

    'installable': True,
    'category': 'Administration',
    'author': 'Pari',
    'application': True
}
