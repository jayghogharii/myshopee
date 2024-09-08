from odoo import fields,models

class Info(models.Model):
    _name="general.information"
    _description = "Add Info"
    
    # connecting_field = fields.Many2one('clg.professor', string="Subject List")
    first_name=fields.Char(required="True")
    middle_name=fields.Char(required="True")
    last_name=fields.Char(required="True")  
    country_id = fields.Many2one('res.country', string="country")
    state_id = fields.Many2one('res.country.state', string="state")
    