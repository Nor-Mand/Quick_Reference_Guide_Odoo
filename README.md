# Quick Reference Guide - ODOO
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)]() 
### `Directories`
- data/: demo and data xml
- models/: models definition
- controllers/: contains controllers (HTTP routes)
- views/: contains the views and templates
- static/: contains the web assets, separated into css/, js/, imag/, lib/,

### `Optional directories`
- wizard/: regroups the transient models (models.TrasientModel) and their views
- report/: contains the printable reports and models based on SQL views. Python objects and XML
- test/: contains the Python tests

### `Tree view of module:`
```
folder/Quick_Reference_Guide_odoo/
|-- __init__.py
|-- __manifest__.py
|-- controllers/
|   |-- ****.py
|-- data/
|   |-- ****.xml
|-- models/
|   |-- __init__.py
|   |-- gallery_art.py 
|-- report/
|   |-- ****.py
|-- security/
|   |-- ir.model.access.csv
|-- static/
|   |-- description/
|   |   |-- icon.png
|-- views/
|   |-- ****.xml
|-- wizards/
|   |-- ****.py
|-- INSTANCE_cheat_sheet.md
|-- MANIFEST_cheat_sheet.md
|-- README.md
```
