from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Admission(models.Model):
    _name = "clg.admission"
    _description = "Admission Form"

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", required=True)
    address = fields.Text(string="Address", required=True)
    document_ids = fields.One2many('clg.admission.document', 'admission_id', string="Documents")
    fees = fields.Float(string="Fees")

    state = fields.Selection([
        ('information', 'Information'),
        ('document', 'Documents'),
        ('fees', 'Fees'),
        ('done', 'Done'),
    ], string='Status', required=True, readonly=True, copy=False, tracking=True, default='information')

    @api.constrains('fees')
    def _check_fees(self):
        if self.state == 'fees' and (not self.fees or self.fees <= 0):
            raise ValidationError("Fees amount must be greater than 0.")

    def button_information(self):
        self.state = 'information'

    def button_document(self):
        self.state = 'document'

    def button_fees(self):
        self.state = 'fees'

    def button_done(self):
        self.state = 'done'


class AdmissionDocument(models.Model):
    _name = "clg.admission.document"
    _description = "Admission Document"

    admission_id = fields.Many2one('clg.admission', string="Admission")
    name = fields.Char(string="Name", required=True)
    attachment = fields.Binary(string="Attachment", required=True)
