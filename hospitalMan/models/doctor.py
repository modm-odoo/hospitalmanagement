from odoo import fields,models

class Doctor(models.Model):
    _name = 'doctor'

    dname = fields.Char("DoctorName")
    speciality = fields.Selection(
        string ="Specialist in",
        selection = [('cardiologist','Cardio-Heart'),('skincare','Skin'),('ent','ENT'),('kneespecialist','Surguon-knee')])
    Patient = fields.Char("PatientName")
    # availableon = time_availability = fields.Date("Date Availability")
