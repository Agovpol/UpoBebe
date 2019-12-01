# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
    _name = 'upobebe.venta'

    name = fields.Char('ID', size=10, required=True,)
    importe = fields.Float('Importe', size=6, required=True)
    fecha = fields.Date('Fecha', required=True, autodate=True)
    comentarios = fields.Text('Comentarios')
    estado = fields.Selection([('en proceso de envio','En proceso de envio'),
                                     ('entregado','Entregado'),],
                                     'Estado')
    cliente_id =  fields.Many2one("upobebe.cliente",string="Cliente")
    articulo_ids = fields.Many2many("upobebe.articulo")
