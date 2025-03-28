{
    'name': 'formulario',
    'version': '1',
    'summary': 'JS Widgets, formulario web para Odoo',
    'description': "",
    'category': 'Custom',
    'author': 'Martin',
    'website': 'google',
    'license': 'AGPL-3',
    'depends': ['base', 'portal', 'web', 'website'],
    'data': [
        'views/templates.xml',
        'views/website_menus.xml',
    ],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_frontend': [
            'website_form/static/src/js/*.js',
            'website_form/static/src/scss/*',
        ],
    }
}
