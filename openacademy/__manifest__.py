{
    'name': 'Open Academy Tutorial',
    'version': '0.1',
    'summary': 'Modulo dl tutorial',
    'description': """
    Long description of the module.
    """,
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'demo/demo.xml',
        'security/ir.model.access.csv',
        'views/actions.xml',
        'views/menus.xml',
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}