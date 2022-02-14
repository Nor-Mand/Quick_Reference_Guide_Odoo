# odoo_plant_nursery | Module odoo guidelines
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
folder/odoo_plant_nursery/
|-- __init__.py
|-- __manifest__.py
|-- controllers/
|   |-- plant_nursery.py
|   |-- portal.py (inheriting portal/controllers/portal.py)
|   |-- main.py (deprecated, replaced by platn_nursey.py
|-- data/
|   |-- plant_nursery_data.xml
|   |-- plant_nursery_demo.xml
|   |-- mail_data.xml
|-- models/
|   |-- plant_nursery.py (first main model)
|   |-- plant_order.py (another main model)
|   |-- res_partner.py (inherited Odoo model)
|-- report/
|   |-- plant_order_report.py
|   |-- plant_order_report_views.xml
|   |-- plant_order_reports.xml (report actions, paperformat,..)
|   |-- plant_order_templates.xml (xml report templates)
|-- security/
|   |-- ir.model.access.csv (the definition of access rights)
|   |-- plant_nursery_groups.xml (user groups are defined)
|   |-- plant_nursery_security.xml (record rules are defined)
|-- static/
|   |-- img
|   |   |-- my_logo.png
|   |   |-- logo.jpg
|   |-- lib/
|   |   |-- external_lib/
|   |-- src/
|   |   |-- js/
|   |   |   |-- widget_a.js
|   |   |   |-- widget_b.js
|   |   |-- scss/
|   |   |   |-- widget_a.scss
|   |   |   |-- widget_b.scss
|   |   |-- xml/
|   |   |   |-- widget_a.xml
|   |   |   |-- widget_b.xml
|-- views/
|   |-- assets.xml (import of JS / CSS)
|   |-- plant_nursery_menu.xml (optional definition of main menus)
|   |-- plant_nursery_views.xml (backend views)
|   |-- plant_templates_views.xml (portal templates
|   |-- plant_order_views.xml
|   |-- plant_order_templates.xml
|   |-- res_partener_views.xml
|-- wizards/
|   |-- make_plant_order.py
|   |-- meke_plant_order_views.xml
```