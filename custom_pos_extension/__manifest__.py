{
    'name': 'Custom Pos Extension',
    'version': '1.0',
    'summary': 'Connecting Different Modules',
    'description': 'Connecting Different Modules',
    'depends': ['base', 'sale', 'website_sale', 'product','web'],
    'data': [
        'views/pos_extension_views.xml',
        'views/product_template.xml',
        'views/sale_order_line_view.xml',
        'views/product_creation_extension.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'custom_pos_extension/static/src/xml/product_popup_custom_field.xml',
        ],
        'web.assets_frontend': [
            'custom_pos_extension/static/src/js/additional_qty.js',
            'custom_pos_extension/static/src/js/website_addToCart.js',
        ],
    },
    'installable': True,
    'category': 'Administration',
    'author': 'Pari',
    'application': True
}
