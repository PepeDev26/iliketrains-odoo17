# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TrainPayment(models.Model):
    _name = 'train.payment'
    _description = 'Registro de Factura de Billetes'

    name = fields.Char(string="Referencia de Factura", required=True)
    provider_id = fields.Many2one('train.provider', string="Proveedor", required=True)
    invoice_date = fields.Date(string="Fecha de Factura", required=True)
    due_date = fields.Date(string="Fecha de Vencimiento")
    total_amount = fields.Float(string="Importe Total")
    
    ticket_ids = fields.One2many('train.ticket', 'payment_id', string="Billetes Incluidos")
    
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('validated', 'Validado'),
        ('paid', 'Pagado'),
    ], string="Estado", default='draft')
    
    payment_date = fields.Date(string="Fecha de Pago")
    payment_reference = fields.Char(string="Referencia de Pago")
    
    notes = fields.Text(string="Notas")
