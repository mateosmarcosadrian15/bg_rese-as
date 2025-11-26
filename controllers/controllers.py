# -*- coding: utf-8 -*-
# from odoo import http


# class BgReseñas(http.Controller):
#     @http.route('/bg_reseñas/bg_reseñas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bg_reseñas/bg_reseñas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bg_reseñas.listing', {
#             'root': '/bg_reseñas/bg_reseñas',
#             'objects': http.request.env['bg_reseñas.bg_reseñas'].search([]),
#         })

#     @http.route('/bg_reseñas/bg_reseñas/objects/<model("bg_reseñas.bg_reseñas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bg_reseñas.object', {
#             'object': obj
#         })

