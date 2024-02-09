from odoo import fields,models

class HospitalManage(models.Model):
    _name = 'hospital_management'

    Patientname = fields.Char("Name",required=True)
    address = fields.Text("Address")
    caseno = fields.Integer("Case")
    problem = fields.Char("Main Problem")
    did = fields.Integer("did")
    
