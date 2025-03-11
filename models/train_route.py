# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TrainRoute(models.Model):
    _name = 'train.route'
    _description = 'Ruta de Tren'

    name = fields.Char(string="Nombre de la Ruta", required=True)
    departure_station_id = fields.Many2one('train.station', string="Estación de Salida", required=True)
    arrival_station_id = fields.Many2one('train.station', string="Estación de Llegada", required=True)
    duration = fields.Float(string="Duración (horas)", help="Duración estimada en horas")
    distance = fields.Float(string="Distancia (km)", help="Distancia en kilómetros")
    
    @api.constrains('departure_station_id', 'arrival_station_id')
    def _check_stations_different(self):
        for route in self:
            if route.departure_station_id == route.arrival_station_id:
                raise ValidationError("La estación de salida y llegada deben ser diferentes.")
