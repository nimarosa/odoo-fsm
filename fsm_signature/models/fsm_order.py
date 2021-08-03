# Copyright (C) 2021 Nimarosa (Nicolas Rodriguez) (<nicolasrsande@gmail.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, _


class FsmOrder(models.Model):
    _inherit = 'fsm.order'

    signed_by = fields.Char(string=(_('Firmado por')))
    signed_on = fields.Datetime(string=(_('Firmado el')))
    signature = fields.Binary(string=(_('Firma')))
