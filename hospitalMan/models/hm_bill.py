from odoo import fields,models

class Bill(models.Model):
    _name = "hospiman.bill"

    patient = fields.Many2one('hospiman.patient')
    casefrompatient = fields.Integer(related="patient.caseno",readonly = True)
    billno = fields.Integer("Bill-No")
    Charges = fields.Integer("Total amount")
