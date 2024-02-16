# -*- coding: utf-8 -*-

from odoo import fields,models,api

class Bill(models.Model):
    _name = "hospital.bill"

    patient = fields.Many2one("hospital.patient", required = True)
    case_from_patient = fields.Char(related="patient.case_no", readonly = True)
    doctor_name = fields.Many2one(related="patient.assign_doc", readonly=True,store=True)
    bill_no = fields.Char("Bill-No")
    charges = fields.Integer("Total Bill")


    @api.model
    def create(self,vals):
        vals['bill_no'] = self.env['ir.sequence'].next_by_code('hospital.bill')
        return super().create(vals)


    
