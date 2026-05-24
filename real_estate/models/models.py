# -*- coding: utf-8 -*-
from odoo import models, fields, api

class real_estate(models.Model):
    _name = 'real_estate.real_estate'
    _description = 'Real Estate Property'

    name = fields.Char(string="Property Name")
    value = fields.Integer(string="Value")
    value2 = fields.Float(compute="_value_pc", store=True, string="Percentage Value")
    description = fields.Text(string="Description")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            if record.value:
                record.value2 = float(record.value) / 100
            else:
                record.value2 = 0.0