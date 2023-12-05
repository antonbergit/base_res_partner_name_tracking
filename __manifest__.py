# -*- coding: utf-8 -*-
{
    # TODO: replace with user-friendly name
    'name': "SPOC Template Module",

    # TODO: replace with breef
    'summary': """
        SPOC Template Module for developers""",

    # TODO: replace with common description (model, views, wizards, etc.)
    'description': """
        SPOC Template Module for developers
    """,

    # TODO: DO NOT CHANGE BLOCK
    'author':       'SPOC',
    'website':      "https://spoc-odoo.com.ua/",
    'company':      'SPOC corp',
    'maintainer':   'SPOC corp',
    'license':      'LGPL-3',
    # TODO: END OF DO NOT CHANGE BLOCK

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # TODO: replace with valid and relative category name
    'category': 'Uncategorized',
    # TODO: iterate this carefully with KISS method
    'version': '15.0.1.0.0',

    # TODO: check and change if necessary
    'installable': True,
    'auto_install': False,
    'application': False,

    # TODO: sync with your inheritance models and views or code relations
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
