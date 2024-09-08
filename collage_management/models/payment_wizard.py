from odoo import models, fields,api

class payment(models.TransientModel):
    _name = 'payment.wizard'
    _description = 'Payment Wizard '
   
    product_id= fields.Many2one('product.product', string='Product')
    fess=fields.Float(string="fess")



    @api.onchange('product_id')
    def onchange_name(self):
        if self.product_id:
            self.fess=self.product_id.list_price

    # Define other fields as needed

    def action_confirm(self):
        
         return{
              'type': 'ir.actions.act_window',
            'name': 'payment',
            'res_model': 'res.partner',
            'view_mode': 'form',
            'target': 'current',
         }
    def discard(self):
        pass
        # return{
        #     'type': 'ir.actions.act_window',
        #     'name': 'collage student',
        #     'res_model': 'clg.student',
        #     'view_mode': 'form',
        #     'state': "document",

        # }