#-*- coding: utf-8 -*-

from odoo import models, Command, fields

class InheritedModelaccountmove(models.Model):
    _inherit = "account.move"
    _name = "account.move"

    partner_id = fields.Many2one('res.partner', readonly=True, tracking=True,
        states={'draft': [('readonly', False)]},
        check_company=True,
        string='Partner', change_default=True)
    patient_id = fields.Many2one("hospital.patient")
