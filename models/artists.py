# -*- coding: utf-8 -*-
from odoo import models,fields


class Artists(models.Model):
    _name = 'gallery.artists'
    _description = 'Gallery artists'
    _rec_name = 'art_style'
    _order = 'date_born desc, name'

    name = fields.Many2one('res.partner', string="Artist Name")
    art_style = fields.Selection([
                    ('IM','Impressionism'),
                    ('CU','Cubism'),
                    ('AB','Abstract'),
                    ('RE','Realism'),
                    ('RO','Romanticism'),
                    ])
    date_born = fields.Date(string='Date of Born')
    date_died = fields.Date(string='Date of dead')