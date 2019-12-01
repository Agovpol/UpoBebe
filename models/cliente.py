# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cliente(models.Model):
    _name = 'upobebe.cliente'

    name =  fields.Char('Nombre', size=60, required=True)
    apellidos =  fields.Char('Apellidos', size=60, required=True)
    dni = fields.Char('DNI', size=9, required=True)
    numero =  fields.Char('Telefono', size=9, required=True)
    direccion = fields.Char('Direccion', size=60, required=True)
    correo = fields.Char('Correo', size=60, required=True)
    cp =  fields.Char('Codigo Postal', size=5, required=True)
    venta_ids = fields.One2many('upobebe.venta','cliente_id', 'Ventas')
