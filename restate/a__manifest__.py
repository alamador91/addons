# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'version': '0.1',
    'category': 'Technical',
    #'sequence': 15,
    'summary': 'Manage real estate offers',
    'description': "Real Estate module",
    'website': 're',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}