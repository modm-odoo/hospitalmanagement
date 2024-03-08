# -*- coding: utf-8 -*-

from odoo import fields,models,api

class Doctor(models.Model):
    _name = "hospital.doctor"

    name = fields.Char("Doctor Name")
    gender = fields.Selection(
        string ="Gender",
        selection = [("male", "Male"),("female", "Female")])
    contact_no = fields.Integer("Contact No")
    department = fields.Selection(
        string ="Department",
        selection = [("cardiologist", "Cardio-Heart"),("skincare", "Skin"),("ent", "ENT"),("kneespecialist", "Surguon-knee")])
    patients_ids = fields.One2many("hospital.patient", "assign_doc_id")
    total_patients = fields.Integer(compute="_compute_patients", store=True)

    @api.depends("patients_ids")
    def _compute_patients(self):
        for doctor in self:
            doctor.total_patients = len(doctor.patients_ids)

