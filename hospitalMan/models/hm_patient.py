from odoo import fields,models

class HospitalManage(models.Model):
    _name = 'hospiman.patient'

    patientname = fields.Char("Name",required=True)
    address = fields.Text("Address")
    gender = fields.Selection(
        string ="Gender",
        selection = [('male','Male'),('female','Female')])
    caseno = fields.Integer("Case",required=True)
    problem = fields.Char("Main Problem")
    assign_doc = fields.One2many('hospiman.doctor','patient')
    roomrequire = fields.Many2one('hospiman.roomfield',required=False)

