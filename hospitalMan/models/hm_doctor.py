from odoo import fields,models

class Doctor(models.Model):
    _name = 'hospiman.doctor'

    dname = fields.Char("DoctorName")
    did = fields.Integer("Doctor Id")
    gender = fields.Selection(
        string ="Gender",
        selection = [('male','Male'),('female','Female')])
    contactno = fields.Integer("contactno")
    department = fields.Selection(
        string ="Specialist in",
        selection = [('cardiologist','Cardio-Heart'),('skincare','Skin'),('ent','ENT'),('kneespecialist','Surguon-knee')])
    patient = fields.Many2one('hospiman.patient')
    # availableon = time_availability = fields.Date("Date Availability")