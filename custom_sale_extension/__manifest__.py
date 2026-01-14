{
    'name': 'Custom Sale Extension',
    'version': '1.0',
    'summary': 'performing inheritance',
    'description': 'Inheritance practice',
    'depends':['base','sale'],
    'data':[
        'security/ir.model.access.csv',
        'views/sale_extension_views.xml',
        'views/custom_order_line_views.xml',
        'views/custom_order_line_wizard_view.xml',
        'views/custom_invoice_views.xml',
        'views/report_custom_order_line.xml',
        'views/report_saleorder_template_inherit.xml',
    ],
    'installable':True,
    'category':'Administration',
    'author': 'Pari',
    'application': True
}