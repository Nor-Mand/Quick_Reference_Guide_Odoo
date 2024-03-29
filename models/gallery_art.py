# -*- coding: utf-8 -*-
from odoo import models, fields


class GalleryArt(models.Model):
    _name = 'gallery.art'
    _description = "Gallery Art"

    name = fields.Char(string="Gallery Name", required=True)
    contact_ids = fields.Many2one('res.partner', string="Contact")
    about = fields.Text(string="About the Gallery")

