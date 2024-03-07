# -*- coding: utf-8 -*-

from odoo import fields,models,api

class Room(models.Model):
    _name = "hospital.room"

    name = fields.Char("Room No")
    room_type = fields.Selection(
        string="Room Type",
        selection=[("ac", "AC - 1000"), ("nonac", "NonAC - 750")], store=True
    )
    price = fields.Integer("Price", compute="_compute_price", store=True)
    allotted_patients = fields.One2many("hospital.patient",inverse_name="room_no")
    total_patients = fields.Integer(compute="_compute_total_patients", store=True)

    @api.depends("allotted_patients")
    def _compute_total_patients(self):
        for record in self:
            record.total_patients = len(record.allotted_patients)

    @api.depends("room_type")
    def _compute_price(self):
        for room in self:
            if room.room_type == "ac":
                room.price = 1000
            elif room.room_type == "nonac":
                room.price = 750

    