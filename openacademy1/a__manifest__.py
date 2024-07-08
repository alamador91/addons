# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Open Academy',
    'version': '16.0.0.0.0',
    'category': 'Tutorial',
    #'sequence': 15,
    'summary': 'Tutorial que sirve summ',
    'description': "Tutorial que sirve desc",
    'website': 'oatuto',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/custom_views.xml',
        'views/menu.xml'
    ],
    'demo': [
        'demo/listado_cursos.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}