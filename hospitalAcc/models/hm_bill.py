#-*- coding: utf-8 -*-

from odoo import models, Command

class InheritedModel(models.Model):
    _inherit = "hospital.bill"

    def action_mark_as_done(self):
        partner = self.env['res.partner'].search([('ref', '=', self.patient_id.id)], limit=1)
        if not partner:
            partner = self.env['res.partner'].create({
                'name': self.patient_id.name,  # Use patient name for partner name
                'ref': self.patient_id.id,  # Link the partner to patient (optional)
                # Add other relevant partner data here (e.g., email, phone)
            })
            # partner_data = self.patient_id.with_context(no_auto_write=True).copy_data({})[0]  # Avoid infinite loop
            # partner_data['patient_id'] = self.patient_id.id  # Link the patient
            # partner = self.env['res.partner'].create(partner_data)
        mov_data = {
            "partner_id" : partner.id,
            "move_type" : "out_invoice",
            "invoice_line_ids": [
                Command.create({
                    "name": self.case_from_patient, "quantity" : 1, "price_unit" : self.medicine_price}),
                Command.create({
                    "name": "Room Charges", "quantity" : 1, "price_unit" : self.room_price}),
            ]
        }
        new_invoice = self.env["account.move"].create(mov_data)
        return super().action_mark_as_done()