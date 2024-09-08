# -*- coding: utf-8 -*-
# from odoo import http


# class CollageManagement(http.Controller):
#     @http.route('/collage_management/collage_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/collage_management/collage_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('collage_management.listing', {
#             'root': '/collage_management/collage_management',
#             'objects': http.request.env['collage_management.collage_management'].search([]),
#         })

#     @http.route('/collage_management/collage_management/objects/<model("collage_management.collage_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('collage_management.object', {
#             'object': obj
#         })

