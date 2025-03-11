# -*- coding: utf-8 -*-
from odoo import models, fields

class TrainStation(models.Model):
    _name = 'train.station'
    _description = 'Estación de Tren'

    name = fields.Char(string="Nombre de la Estación", required=True)
    location = fields.Char(string="Ubicación", required=True)
