from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class Collage(http.Controller):

    @http.route('/information',type="http",auth="public",website=True)
    def information(self,**kw):
        return http.request.render('collage_management.general_info',{})

    
    
    @http.route('/create/generalinfo',type="http",auth="public",website=True)

    def create_generalinfo(self,**kw):

        request.env['general.information'].sudo().create(kw)
        return request.render("collage_management.student_thanks",{})
    


   