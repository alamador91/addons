# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate',
    'version': '16.0.0.0.1',
    'category': 'Technical',
    'sequence': 15,
    'summary': 'Real Estate advertisement',
    'description': "Real Estate advertisement",
    'website': 'https://achel.000.pe',
    'depends': [
        'base',
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',

        #'data/crm_lead_prediction_data.xml',
        #'wizard/crm_merge_opportunities_views.xml',

        'views/main_menu.xml',
        'views/test_model_views.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/res_user_views.xml',
    ],
    'demo': [
        #'data/crm_team_demo.xml',
        #'data/mail_activity_demo.xml',
        #'data/crm_lead_demo.xml',
    ],
    'css': ['static/src/css/crm.css'],
    'installable': True,
    'application': True,
    'auto_install': False
}
