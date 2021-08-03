# Copyright (C) 2021 Nimarosa (Nicolas Rodriguez) (<nicolasrsande@gmail.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class FsmOrder(models.Model):
    """
    Add many images to the fsm order. Not used in backend view, only shown. 
    TODO: Make some approach to upload from backend in some cases. 
    """
    _inherit = 'fsm.order'

    fsm_order_onfield_image_ids = fields.Many2one('fsm.order.fsm_order_onfield_image', string=(_('Imagenes de Campo')))


class FsmOnfieldImage(models.Model):
    """
    This class is used to store individually images 
    attached to the fsm_order from on field employees. 
    """
    _name = 'fsm.order.onfield_image'
    _description = 'Stores on field uploaded images to the fsm order.'

    blob = fields.Binary(string=(_('Imagen')))
