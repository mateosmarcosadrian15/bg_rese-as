# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Usuarios(models.Model):
    _name = 'bg_resenas.usuario'
    _description = 'Usuarios'
    _rec_name='nombreUsuario'

    nombreUsuario = fields.Char(string='Nombre de Usuario',required=True)
    email = fields.Char(string='Email',required=True)
    telefono = fields.Char(string='Telefono')

    juego_id = fields.Many2one('bg_juegos.juego',string='Juegos')

class Reseñas(models.Model):
    _name='bg_resenas.resena'
    _description= 'Reseñas'
    _rec_name = 'nombre'

    nombre = fields.Char(string= 'nombre',default="Reseña")
    puntuacion = fields.Integer(string='Puntuacion',required=True)
    comentario = fields.Char(string='Comentario')

    usuario_id = fields.Many2one('bg_resenas.usuario',string='Usuario')

# class bg_reseñas(models.Model):
#     _name = 'bg_reseñas.bg_reseñas'
#     _description = 'bg_reseñas.bg_reseñas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

