# Copyright (C) 2021 Nimarosa (Nicolas Rodriguez) (<nicolasrsande@gmail.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class FsmOrder(models.Model):
    _inherit = 'fsm.order'

    fsm_onfield_media_files = fields.One2many('fsm.order.onfield_media_file', 'fsm_order_id', string='Imagenes de Campo')


class FsmOrderOnfieldMediaFile(models.Model):
    _name = 'fsm.order.onfield_media_file'
    _description = 'Stores on field uploaded images to the fsm order.'

    file = fields.Binary(string="Archivo")
    file_description = fields.Char(string="Descripcion")
    fsm_order_id = fields.Many2one('fsm.order', string='Orden de FSM')
