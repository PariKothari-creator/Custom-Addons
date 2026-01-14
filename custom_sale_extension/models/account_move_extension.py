# -*- coding: utf-8 -*-
from odoo import models,fields


class AccountMoveExtension(models.Model):
    _inherit = 'account.move'


    custom_invoice_line_ids = fields.One2many('custom.invoice','invoice_id')

