# -*- coding: utf-8 -*-

from odoo import fields,models,api
from datetime import date

class HospitalManage(models.Model):
    _name = "hospital.patient"

    name = fields.Char("Name", required=True)
    address = fields.Text("Address")
    gender = fields.Selection(
        string ="Gender",
        selection = [('male','Male'),('female','Female')])
    date_of_birth = fields.Date("Date Of Birth")
    age = fields.Integer(compute="compute_age",tracking=True,store=True)
    case_no = fields.Char("Case No")
    problem = fields.Char("Main Problem")
    assign_doc = fields.Many2one("hospital.doctor", required=True)
    client_image = fields.Image('Image', max_width=1920, max_height=1920)   
     
    @api.model
    def create(self,vals):
        vals['case_no'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super().create(vals)

    @api.depends("date_of_birth")
    def compute_age(self):
        for rec in self:
            today = date.today()

            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age=1
            