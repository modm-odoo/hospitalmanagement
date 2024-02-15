# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'HospitalManagement',
    'description' : 'this is the description',
    'version' : '1.0',
    'summary': 'The best app for hospital management',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'depends':['base'],
    'data':[
        "security/ir.model.access.csv",
        "views/hm_bill_view.xml",
        "views/hm_doctor_view.xml",
        "views/hm_patient_view.xml",
        "views/hm_room_view.xml",
        "views/hm_menu.xml",
    ],
}