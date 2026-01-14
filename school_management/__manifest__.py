{
    'name': 'School Management',
    'version': '1.0',
    'summary': 'Manages Students Records',
    'description': 'Compelete record of school management',
    'depends':['base','hr','sale'],
    'data':[
        'security/school_security.xml',
        'security/ir.model.access.csv',
        'views/school_subject_view.xml',
        'views/school_class_view.xml',
        'views/school_student_view.xml',
        'views/school_exam_view.xml',
        'views/exam_subjects.xml',
        'views/student_menu_view.xml'
    ],
    'installable':True,
    'category':'Administration',
    'author': 'Pari',
    'application': True
}