# -*- coding: utf-8 -*-
{
    'name': "FaceBase",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "DA (Chinh.chutrieu)",
    'website': "http://www.dacompany.com.vn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'attendance_log', 'hr_employee'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/facebase_data.xml',
        'views/facebase_view.xml',
        'views/facebase_resources_view.xml',
        'views/assets.xml',
        'views/menu.xml',
    ],
    'qweb': [
        "static/src/xml/operate_button.xml",
    ],
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': True,

}