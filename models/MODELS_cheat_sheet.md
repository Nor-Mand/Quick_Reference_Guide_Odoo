### `Models`
- It has structural attributes for defining their behavior

### `Basic Structure:`
```commandline
folder/Quick_Reference_Guide_odoo/models/
|-- models/
|   |-- __init__.py
|   |-- gallery_art.py 
```

### `Important attributes of the model:`

| attribute    | type | description                                   |
|--------------|------|-----------------------------------------------|
| _name        | None | the model name (in dot-notation, module namespace) |
| _description | None | the model’s informal name                     |
| _inherit     | ()   | Python-inherited models                       |
| _rec_name    | None | field to use for labeling records             |
| _order       | 'id'   | default order field for searching results     |          

### `Basic Fields:`
| name    | type  |
|---------|-------|
| Boolean | bool  |
| Char    | char  |
| Float   | float |
| Integer | Int   |

### `Advanced Fields:`
| name      | type                 |
|-----------|----------------------|
| Binary    | binary               |
| Html      | text                 |
| Image     | binary               |
| Monetary  | float                |
| Selection | list(tuple(str,str)) |
| Text      | text                 |
| Datetime  | datetime             |
| Date      | date                 |

### `Parameters (Fields)`
| name              | type  | description|
|-------------------|-------|-|
| string            | str   ||
| help              | str   ||
| readonly          | bool  ||
| required          | bool  ||
| index             | str   ||
| default           | value ||
| groups            | str   ||
| company_dependent | bool  ||
| copy              | bool  ||
| store             | bool  ||