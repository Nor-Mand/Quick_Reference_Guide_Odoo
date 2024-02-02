{
    'name': "Nordoo Art Gallery",
    'version': '1.0',
    'summary': 'Quick Reference Guide',
    'description': """
        Nordoo Art Gallery is a quick reference guide to using all the features that come with odoo, you can use this module as a reference.
    """,
    'author': "Normand Terceros",
    'website': "https://normand.dev",
    'category': "Art",
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "views/gallery_view.xml",
        "views/artist_view.xml",
        "views/gallery_menus.xml",
    ],
    'installable': True,
    'application': True,
}
# -*- coding: utf-8 -*-
