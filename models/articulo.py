# -*- coding: utf-8 -*-

from odoo import models, fields, api

class articulo(models.Model):
    _name = 'upobebe.articulo'

    name =  fields.Char('Nombre', size=70, required=True)
    precio = fields.Float('Precio por unidad', size=6, required=True)
    foto = fields.Binary('Foto') 
    descripcion = fields.Text('Descripcion')
    id = fields.Char('ID', size=4, required=True)
    venta_ids = fields.Many2many('upobebe.venta', string='Ventas de las que forma parte')  
