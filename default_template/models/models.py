# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class default_template(models.Model):
#     _name = 'default_template.default_template'
#     _description = 'default_template.default_template'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

