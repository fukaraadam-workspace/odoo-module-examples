# -*- coding: utf-8 -*-
# from odoo import http


# class DefaultTemplate(http.Controller):
#     @http.route('/default_template/default_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/default_template/default_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('default_template.listing', {
#             'root': '/default_template/default_template',
#             'objects': http.request.env['default_template.default_template'].search([]),
#         })

#     @http.route('/default_template/default_template/objects/<model("default_template.default_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('default_template.object', {
#             'object': obj
#         })

