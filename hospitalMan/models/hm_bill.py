from odoo import fields,models

class Bill(models.Model):
    _name = "hospiman.bill"

    patient = fields.Many2one('hospiman.patient')
    casefrompatient = fields.Many2one('hospiman.patient', string="Case from Patient", related='patient', store=True)
    billno = fields.Integer("Bill-No")
    Charges = fields.Integer("Total amount")
