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
    ],
}