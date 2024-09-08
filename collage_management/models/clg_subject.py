from odoo import fields,models

class AddSubject(models.Model):
    _name="clg.subject"
    _description = "Add Subject"
    
    # connecting_field = fields.Many2one('clg.professor', string="Subject List")
    subject=fields.Char(required="True")
    
    