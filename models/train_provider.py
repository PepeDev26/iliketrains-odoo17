# -*- coding: utf-8 -*-
from odoo import models, fields

class TrainProvider(models.Model):
    _name = 'train.provider'
    _description = 'Proveedor de Servicios de Tren'

    name = fields.Char(string="Nombre del Proveedor", required=True)
    code = fields.Char(string="Código", help="Código identificador del proveedor")
    website = fields.Char(string="Sitio Web")
    active = fields.Boolean(string="Activo", default=True)
    notes = fields.Text(string="Notas")
    ticket_ids = fields.One2many('train.ticket', 'provider_id', string="Billetes")
