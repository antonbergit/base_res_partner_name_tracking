from odoo import models, fields


class Partner(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(track_visibility='always')
  
