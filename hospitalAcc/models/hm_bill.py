#-*- coding: utf-8 -*-

from odoo import models, Command

class InheritedModel(models.Model):
    _inherit = "hospital.bill"

    def action_mark_as_done(self):
        # breakpoint()
        mov_data = {
            "partner_id" : self.name,
            "move_type" : "out_invoice",
            "invoice_line_ids": [
                Command.create({
                    "name": self.case_from_patient, "quantity" : 1, "price_unit" : self.total_bill}),
                Command.create({
                    "name": "Room Charges", "quantity" : 1, "price_unit" : 100}),
            ]
        }
        new_invoice = self.env["account.move"].create(mov_data)
        return super().action_mark_as_done()