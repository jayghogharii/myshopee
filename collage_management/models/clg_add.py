from odoo import fields,models

class AddCollage(models.Model):
    _name="clg.add"
    _description = "Add Collage"
    _rec_name = "collagename"

    collagename=fields.Char("collagename",required="True")
    email = fields.Char(string='Email', required=True)
    address = fields.Text(string='Address',required="True")
    conno = fields.Char(string='Contact Number',required="True")
    