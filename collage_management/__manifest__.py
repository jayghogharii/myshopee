# -*- coding: utf-8 -*-
{
    'name': "collage_management",

    'summary': "clg_management",

    'description': """
Welcome to My collage Admission is open now In Bca,Mca,Btech,Mtech 
    """,

    'author': "Jay_Ghoghari",
    'website': "https://www.collage.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','base_setup'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
          'security/security.xml',
          'views/clg_students_views.xml',
          'views/clg_department.xml',
         'views/clg_add.xml',
         'views/clg_subject.xml',
        'views/professor.xml',
         'views/check.xml',
         'views/payment_wizard.xml',
         'views/payment_invoice.xml',
         'views/schedule_action.xml',
         'views/website_form.xml',
         'views/general_information.xml',
#         'static/src/style.css',  # Include your CSS file here
        
        
    ],
    # only loaded in demonstration mode
    # 'demo': [
        # 'demo/demo.xml',
    # ],
}

