# -*- coding: utf-8 -*-

from odoo import fields,models,api

class Bill(models.Model):
    _name = "hospital.bill"

    patient_id = fields.Many2one("hospital.patient", string="Patient", required = True)
    case_from_patient = fields.Char(related="patient_id.case_no", readonly = True)
    doctor_name_id = fields.Many2one("hospital.doctor", related="patient_id.assign_doc_id", readonly=True, store=True)
    bill_no = fields.Char("Bill-No")
    room_no = fields.Many2one(related="patient_id.room_no") 
    room_type = fields.Selection(related="patient_id.room_type")
    room_price = fields.Integer(related="patient_id.room_price")
    medicine_price = fields.Integer("Medicine Cost")
    total_bill = fields.Integer("Total Bill", compute="_compute_total_bill", store=True)

    @api.depends("room_price", "medicine_price")
    def _compute_total_bill(self):
        for record in self:
            record.total_bill = record.room_price + record.medicine_price

    @api.model
    def create(self,vals):
        vals["bill_no"] = self.env["ir.sequence"].next_by_code("hospital.bill")
        return super().create(vals)



    
