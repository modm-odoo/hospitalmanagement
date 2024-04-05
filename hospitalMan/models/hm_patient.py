# -*- coding: utf-8 -*-

from odoo import fields, models, api
from datetime import datetime, timedelta, date

class HospitalManage(models.Model):
    _name = "hospital.patient"

    name = fields.Char("Name", required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', ondelete='cascade')
    address = fields.Text("Address")
    gender = fields.Selection(
        string ="Gender",
        selection = [("male", "Male"),("female", "Female")])
    date_of_birth = fields.Date("Date Of Birth")
    age = fields.Integer(compute="compute_age", store=True)
    case_no = fields.Char("Case No")
    problem = fields.Char("Main Problem")
    assign_doc_id = fields.Many2one("hospital.doctor", required=True)
    client_image = fields.Image("Image", max_width=1920, max_height=1920)  
    room_no = fields.Many2one("hospital.room")
    room_type = fields.Selection(related="room_no.room_type")
    room_price = fields.Integer(related="room_no.price")
    start_date = fields.Datetime(string="Appointment Date", store=True)
    end_date = fields.Datetime(string="End Date", compute="_compute_end_date", store=True)

    @api.depends("start_date")
    def _compute_end_date(self):
        for record in self:
            if record.start_date:
                end_date = record.start_date + timedelta(hours=2)
                record.end_date = end_date
            else:
                record.end_date = False

    @api.depends("date_of_birth")
    def compute_age(self):
        for rec in self:
            today = date.today()

            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age=1
    
    @api.model
    def create(self,vals):
        vals["case_no"] = self.env["ir.sequence"].next_by_code("hospital.patient")
        return super().create(vals)