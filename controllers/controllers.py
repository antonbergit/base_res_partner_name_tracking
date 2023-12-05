# -*- coding: utf-8 -*-
# from odoo import http


# class SpocTemplate(http.Controller):
#     @http.route('/spoc_template/spoc_template', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/spoc_template/spoc_template/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('spoc_template.listing', {
#             'root': '/spoc_template/spoc_template',
#             'objects': http.request.env['spoc_template.spoc_template'].search([]),
#         })

#     @http.route('/spoc_template/spoc_template/objects/<model("spoc_template.spoc_template"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('spoc_template.object', {
#             'object': obj
#         })
