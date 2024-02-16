# -*- coding: utf-8 -*-

from odoo import fields,models

class Doctor(models.Model):
    _name = "hospital.doctor"

    name = fields.Char("Doctor Name")
    gender = fields.Selection(
        string ="Gender1",
        selection = [("male","Male"),("female","Female")])
    contact_no = fields.Integer("Contact No")
    department = fields.Selection(
        string ="Specialist in",
        selection = [("cardiologist","Cardio-Heart"),("skincare","Skin"),("ent","ENT"),("kneespecialist","Surguon-knee")])
    patients = fields.One2many("hospital.patient","assign_doc")
