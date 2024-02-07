from odoo import fields,models

class Room(models.Model):
    _name = "room"

    roomno = fields.Integer("RoomNo")
    Allotto = fields.Char("Name",required=True)
    roomtype = fields.Selection(
        string ="RoomType",
        selection = [('ac','AC'),('nonac','NonAC')])
    price = fields.Integer("Price")