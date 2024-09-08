from odoo import fields,models,api

class invoice(models.Model):
    _name = 'payment.invoice'
    _description = 'Payment invoice '
   
    partner_id=fields.Many2one('account.move',string="Student Name")
    

