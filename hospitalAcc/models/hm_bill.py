#-*- coding: utf-8 -*-

from odoo import models, Command

class InheritedModel(models.Model):
    _inherit = "hospital.bill"

    def action_mark_as_done(self):
        # breakpoint()
        mov_data = {
            "patient_id" : self.patient_id.id,
            "move_type" : "out_invoice",
            "invoice_line_ids": [
                Command.create({
                    "name": self.case_from_patient, "quantity" : 1, "price_unit" : self.medicine_price}),
                Command.create({
                    "name": "Room Charges", "quantity" : 1, "price_unit" : self.room_price}),
                Command.create({
                    "name": self.bill_no, "quantity" : 1, "price_unit" : self.total_bill})
            ]
        }
        new_invoice = self.env["account.move"].create(mov_data)
        return super().action_mark_as_done()