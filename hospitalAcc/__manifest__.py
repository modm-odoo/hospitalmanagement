# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "HospitalManagement2",
    "description": "this is the description",
    "version": "1.0",
    "summary": "The best app for hospital management",
    "installable": True,
    "application": True,
    'module_type': 'official',
    "license": "OEEL-1",
    "depends":["base", "account", "hospitalMan"],
    "data": [
        "security/ir.model.access.csv",
        "views/customer_view.xml",
    ]
}