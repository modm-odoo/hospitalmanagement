from odoo import fields,models

class Room(models.Model):
    _name = "hospiman.roomfield"

    roomno = fields.Integer("RoomNo")
    allotto = fields.One2many('hospiman.patient','roomrequire')
    roomtype = fields.Selection(
        string ="RoomType",
        selection = [('ac','AC'),('nonac','NonAC')])
    price = fields.Integer("Price")

    