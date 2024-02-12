# -*- coding: utf-8 -*-

from odoo import fields,models

class Bill(models.Model):
    _name = "hospital.bill"

    patient = fields.Many2one("hospital.patient", required = True)
    case_from_patient = fields.Integer(related="patient.case_no", readonly = True)
    doctor_name = fields.Integer(related="patient.assign_doc", readonly = True)
    bill_no = fields.Integer("Bill-No")
    charges = fields.Integer("Total amount")
