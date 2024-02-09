from odoo import fields,models

class Bill(models.Model):
    _name = "bill"

    billno = fields.Integer("Bill-No")
    Charges = fields.Integer("Total amount")
    