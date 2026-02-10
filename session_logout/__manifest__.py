{
    'name': 'Session Logout',
    'version': '1.0',
    'summary': 'Session Logout Timer',
    'description': 'Session Logout Timer',
    'depends': ['base', 'sale', 'website_sale', 'product','web'],
    'data': [
        'views/user_timer_enable_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'session_logout/static/src/js/session_logout_timer.js',
            'session_logout/static/src/xml/session_logout.xml'
        ],
    },
    'installable': True,
    'category': 'Administration',
    'author': 'Pari',
    'application': True
}
