# -*- coding: utf-8 -*-

from odoo import fields,models,api

class Room(models.Model):
    _name = "hospital.room"

    room_no = fields.Integer("Room No")
    # _sql_constraints = [
    #     ('unique_room_no', 'unique(room_no)', 'Room No must be unique.')
    # ]
    # @api.constrains('room_no')
    # def _check_room_no(self):
    #     if self.room_no < 1 or self.room_no > 20:
    #         raise ValidationError("Room No must be between 1 and 20.")

    allot_to = fields.Many2one('hospital.patient')
    room_type = fields.Selection(
        string="Room Type",
        selection=[('ac', 'AC - 1000'), ('nonac', 'NonAC - 750')]
    )
    price = fields.Integer("Price", compute='_compute_price', store=True)

    @api.depends('room_type')
    def _compute_price(self):
        for room in self:
            if room.room_type == 'ac':
                room.price = 1000
            elif room.room_type == 'nonac':
                room.price = 750

    