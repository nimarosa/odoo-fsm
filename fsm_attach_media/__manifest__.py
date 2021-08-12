# Copyright (C) 2021 Nimarosa (Nicolas Rodriguez) (<nicolasrsande@gmail.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'FSM Attach Media',
    'version': '13.0.1.0.0',
    'description': 'FSM module to support attaching images to the order',
    'summary': 'FSM module to support attaching images to the order',
    'author': 'Nimarosa',
    'website': 'www.github.com/nimarosa/fsm/fsm_attach_media',
    'license': 'LGPL-3',
    'category': 'Field Service',
    'depends': [
        'fieldservice'
    ],
    'data': [
        'views/fsm_order.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}