# -*- coding: utf-8 -*-

from odoo import fields,models

class Room(models.Model):
    _name = "hospital.room"

    roomno = fields.Integer("RoomNo")
    allot_to = fields.Many2one('hospital.patient')
    roomtype = fields.Selection(
        string ="RoomType",
        selection = [('ac','AC'),('nonac','NonAC')])
    price = fields.Integer("Price")

    