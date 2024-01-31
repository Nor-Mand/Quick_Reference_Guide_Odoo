# -*- coding: utf-8 -*-
from odoo import models, fields


class GalleryArt(models.Model):
    _name = 'gallery.art'

    name = fields.Char()

    #