# -*- coding: utf-8 -*-
{
    'name': "Sale order version",

    'summary': """
    Add version number on sale order
        """,

    'description': """
        
    """,

    'author': "Adquat",
    'website': "http://www.aqdquat.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],
    'license': 'LGPL-3',
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'images': ['static/description/icon_versions_devis.png'],
}