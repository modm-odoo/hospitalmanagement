# -*- coding: utf-8 -*-

from odoo import fields,models

class HospitalManage(models.Model):
    _name = "hospital.patient"

    patient_name = fields.Char("Name", required=True)
    address = fields.Text("Address")
    gender = fields.Selection(
        string ="Gender",
        selection = [('male','Male'),('female','Female')])
    case_no = fields.Integer("Case", required=True)
    problem = fields.Char("Main Problem")
    assign_doc = fields.Many2one("hospital.doctor", required=True)
    # room_require = fields.Many2one("hospital.roomfield",required=False)

