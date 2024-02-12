# -*- coding: utf-8 -*-

from odoo import fields,models

class Doctor(models.Model):
    _name = "hospital.doctor"

    doctor_name = fields.Char("DoctorName")
    gender = fields.Selection(
        string ="Gender",
        selection = [("male","Male"),("female","Female")])
    contact_no = fields.Integer("contactno")
    department = fields.Selection(
        string ="Specialist in",
        selection = [("cardiologist","Cardio-Heart"),("skincare','Skin"),("ent","ENT"),("kneespecialist","Surguon-knee")])
    patients = fields.One2many("hospital.patient","assign_doc")
    # availableon = time_availability = fields.Date("Date Availability")
