### `Manifest`
- It is a file called `__manifest__.py`, contains a single python dictionary.
- The followin is the composition you need to know in order to fill correctly

### `Available fields :`
| name                                  | type                  | required | defaults  |
|---------------------------------------|-----------------------|----------|-----------|
| name                                  | *str*                 | *yes*    |           |
| version                               | *str*                 | *no*     |           |
| description                           | *str*                 | *no*     |           |
| author                                | *str*                 | *no*     |           |
| website                               | *str*                 | *no*     |           |
| license                               | *str*                 | *no*     | LGPL-3    |
| category                              | *str*                 | *no*     | Uncategorized |
| depends                               | *list: str*           | *no*     |           |
| data                                  | *list: str*           | *no*     |           |
| demo                                  | *list: str*           | *no*     |           |
| auto_install                          | *bool or list: str*   | *no*     | False     |
| external_dependencies                 | *dict(key=list: str)* | *no*     |           |
| application                           | *bool*                | *no*     | False     |
| assets                                | *dict*                | *no*     |           |
| installable                           | *bool*                | *no*     | True      |
| maintainer                            | *str*                 | *no*     |           |
| {pre_init, post_init, uninstall}_hook | *str*                 | *no*     |           |
| auto_install                          | *bool*                | *no*     |           |


#### `example:`
````commandline
{
    'name': "name of module",
    'version: '1.0',
    'depends': ['base'],
    'author': "author name",
    'category': "category name",
    'description': """
        Full description about the module
    """,
    'data': [
        "views/name_template_view.xml,
    ],
    'demo': [
        'demo/name_template_data.xml,
    ],
}
````