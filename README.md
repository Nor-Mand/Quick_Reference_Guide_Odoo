# odoo_plant_nursery | Module odoo guidelines
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)]() 
### `Directories`
- data/: demo and data xml
- models/: models definition
- controllers/: contains controllers (HTTP routes)
- views/: contains the views and templates
- static/: contains the web assets, separated into css/, js/, imag/, lib/,

###`Optional directories`
- wizard/: regroups the transient models (models.TrasientModel) and their views
- report/: contains the printable reports and models based on SQL views. Python objects and XML
- test/: contains the Python tests

### `Tree view of module:`
```
folder/odoo_plant_nursery/
|-- models/
|   |-- plant_nursery.py (first main model)
|   |-- plant_order.py (another main model)
|   |-- res_partner.py (inherited Odoo model)
|-- security/
|   |-- ir.model.access.csv (the definition of access rights)
|   |-- plant_nursery_groups.xml (user groups are defined)
|   |-- plant_nursery_security.xml (record rules are defined)
```