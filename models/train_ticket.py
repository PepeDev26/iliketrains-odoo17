# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TrainTicket(models.Model):
    _name = 'train.ticket'
    _description = 'Billete de Tren Externo'

    name = fields.Char(string="Referencia", required=True, help="Número o referencia del billete")
    ticket_code = fields.Char(string="Código de Billete", help="Código identificador único del billete")
    employee_id = fields.Many2one('hr.employee', string="Empleado", required=True)
    provider_id = fields.Many2one('train.provider', string="Proveedor", required=True)
    route_id = fields.Many2one('train.route', string="Ruta", required=True)
    travel_date = fields.Date(string="Fecha de viaje", required=True)
    price = fields.Float(string="Precio", required=True)
    currency_id = fields.Many2one('res.currency', string="Moneda", default=lambda self: self.env.company.currency_id)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
        ('reimbursed', 'Reembolsado'),
        ('cancelled', 'Cancelado'),
    ], string="Estado", default='draft')
    
    # Campos para el archivo del billete
    ticket_file = fields.Binary(string="Archivo de Billete", attachment=True)
    ticket_filename = fields.Char(string="Nombre del archivo de billete")
    
    payment_id = fields.Many2one('train.payment', string="Factura", ondelete='set null')
    invoice_number = fields.Char(string="Número de Factura", related="payment_id.name", store=True, readonly=True)
    invoice_date = fields.Date(string="Fecha de Factura", related="payment_id.invoice_date", store=True, readonly=True)
    invoice_file = fields.Binary(string="Archivo de Factura")
    invoice_filename = fields.Char(string="Nombre del archivo")
    
    notes = fields.Text(string="Notas")
    
    @api.constrains('price')
    def _check_price_positive(self):
        for ticket in self:
            if ticket.price <= 0:
                raise ValidationError("El precio debe ser mayor que cero.")
