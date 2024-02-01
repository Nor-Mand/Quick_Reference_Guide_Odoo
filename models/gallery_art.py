# -*- coding: utf-8 -*-
from odoo import models, fields


class GalleryArt(models.Model):
    _name = 'gallery.art'
    _description = "Gallery Art"

    name = fields.Char(string="Gallery Name", required=True)

