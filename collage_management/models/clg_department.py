from odoo import fields,models


class department(models.Model):
    _name="clg.department"
    _description="This is Collage Department"
    _rec_name = "department"

    department = fields.Char(string="department",required="True")
    batches = fields.Integer(string="batches",required="True")
    
  

    



   

