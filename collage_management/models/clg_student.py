from odoo import fields,models,api
import base64
from odoo.exceptions import ValidationError
import PyPDF2
from io import BytesIO
from odoo.exceptions import UserError
import re

class students(models.Model):
    _name="clg.student"
    _description="This is Student Profile"
    _inherit=['mail.thread','mail.activity.mixin']

    
    # connecting_field = fields.Many2one('clg.professor', string="List")
    collage = fields.Many2one('clg.add', string='collage')
    name=fields.Char()
    middlename=fields.Char(searchable=True)
    lastname=fields.Char(searchable=True)
    gender = fields.Selection([('male', 'Male'), 
                               ('female', 'Female'), 
                               ('other', 'Other')], string='Gender',)
    birthdate = fields.Date(string='DOB',)
    department = fields.Many2one('clg.department', string="Department",searchable=True)
    country_id = fields.Many2one('res.country', string="country")
    state_id = fields.Many2one('res.country.state', string="State", store=True)
    city=fields.Char("city")
    zip=fields.Char()
    email = fields.Char(string='Email', )
    street = fields.Text(string='Address',)
    street2= fields.Text(string='street',)
    mono = fields.Char(string='Contact Number',)
    passport=fields.Binary()
    aadhar_card=fields.Binary(string='Aadhar card',)
    pan_card=fields.Binary(string='Pan card',)
    marksheet_10th=fields.Binary(string='10th marksheet',)
    marksheet_12th=fields.Binary(string='12th marksheet',)
    acno=fields.Integer(string = "Account_No",)
    ifsc_code=fields.Char(string = "IFSC_CODE" , )
    branch_name=fields.Char(string="Branch_name" , )
    amount=fields.Integer(string="Amount" , )
    partner_id = fields.Many2one('res.partner', string='Partner',readonly="True")
    product_id= fields.Many2one('product.product', string='Product')
    fess=fields.Float(string="fess")
    record_count=fields.Integer(compute="compute_count")
    namee=fields.Many2many('clg.professor',string="Professor_name")
    
    @api.depends('name', 'middlename', 'lastname')
    def _compute_appendname(self):
          for record in self:
            full_name_parts = [record.name, record.middlename, record.lastname]
            record.appendname = ' '.join(filter(None, full_name_parts))


    appendname = fields.Char(string='Full Name', compute='_compute_appendname')

    @api.onchange('product_id')
    def onchange_name(self):
        if self.product_id:
            self.fess=self.product_id.list_price

    # def custom_method(self):
    # # Example custom logic: Update a related record when the activity is completed
    #     for activity in self:
    #         if activity.state == 'done' and activity.res_id:
    #             related_record = self.env[activity.res_model].browse(activity.res_id)
    #             related_record.write({'custom_field': activity.custom_field})
        
    # @api.onchange('partner_id')
    # def select_partner(self):
    #     if self.state == 'payment':
    #          self.partner_id=
            

    def action(self):
         if self.name:
              return{ }

    @api.onchange('country_id')
    def set_values_to(self):
            if self.country_id:
                ids = self.env['res.country.state'].search([('country_id', '=', self.country_id.id)])
                return {
                    'domain': {'state_id': [('id', 'in', ids.ids)],}
                }

    state = fields.Selection(selection=[
             ('information', 'Information'),
             ('document', 'Document'),
             ('payment', 'Payment'),
             ('done', 'Done'),
            ],string='Status', readonly=True, copy=False,
                tracking=True, default='information')
    
  
    def information(self):
         self.write({'state':"information"})

    def doc(self):
         self.write({'state':"information"})
    def doc_do(self):
         self.write({'state':"information"})
        
    def button_done(self):
        self.write({'state': "done"})
        missing_fields = []
        for field_name in ['product_id','fess']:
            if not self[field_name]:
                missing_fields.append(field_name)
            if missing_fields:
                error_message = "Oops! You forgot to fill in some mandatory fields. Please provide the following information:\n"
                for field in missing_fields:
                    error_message += f"- {field.capitalize()}\n"
                raise ValidationError(error_message)
        invoice_lines_vals = []
        for record in self:
            invoice_line_vals = (0, 0, {
                'name': record.appendname,
                'product_id': record.product_id.id,
                'price_unit': record.fess,
            })
            invoice_lines_vals.append(invoice_line_vals)

            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': self.partner_id.id,
                'invoice_date': fields.Date.today(),
                'invoice_line_ids': invoice_lines_vals,
            })
            if invoice:
                    invoice.action_post()
                                
    
    def button_document(self):                    
        self.write({'state': "document"})
        self.ensure_one()
        if not self.partner_id:
            partner = self.env['res.partner'].create(
                    {   'name': self.appendname,
                        'phone':self.mono,
                        'street':self.street,
                        'street2':self.street2,
                        'city':self.city,
                        'zip':self.zip,
                    #   'state_id':state.id,
                    #   'country_id':country_id.id,
                        'email':self.email
                    })
            self.partner_id = partner.id
            
        return {
                
            'visible':"state = 'button_payment'" ,
            'readonly': 'True'
        }

    def button_payment(self):
           missing_fields = []
           for field_name in ['aadhar_card','pan_card','marksheet_10th','marksheet_12th']:
                if not self[field_name]:
                    missing_fields.append(field_name)

                if missing_fields:
                  error_message = "Oops! You forgot to fill in some mandatory fields. Please provide the following information:\n"
                  for field in missing_fields:
                        error_message += f"- {field.capitalize()}\n"
                  raise ValidationError(error_message)
                else:
                    self.write({'state': "payment"})

    @api.onchange('name')
    def compute_count(self): 
        for record in self:
            if record: 
                record.record_count = self.env['account.move'].search_count([('invoice_partner_display_name', '=', record.appendname)])
            else: 
                record.record_count = 0

    def student_record(self):
        self.ensure_one()
        for record in self:
            if record:
                return{ 'name': ('Invoices'),
                        'type': 'ir.actions.act_window', 
                        'res_model': 'account.move', 
                        'view_mode': 'tree',
                        'target':'current',
                        'view': [self.env.ref('account.view_out_invoice_tree').id, 'tree'],
                        'domain':[('invoice_partner_display_name','=',record.appendname)],  
                      }

    def open_pdf_file(self):
        attachment = self.env['ir.attachment'].search([
            ('res_model', '=', 'clg.student'),
            ('res_id', '=', self.id),
            ('mimetype', '=', 'application/pdf')
        ], limit=1)

        if attachment:
            try:
                pdf_content = base64.b64decode(attachment.datas)
                pdf_reader = PyPDF2.PdfFileReader(BytesIO(pdf_content))

                if pdf_reader.numPages > 0:
                    page = pdf_reader.getPage(0)
                    pdf_text = page.extractText()
                    # ifsc_account_pattern = re.compile(r'SB No\s*(\d{0,9})')
                    # # pattern=re.compile(r"SB No[a-zA-Z]+\s")
                    # match=ifsc_account_pattern.findall(pdf_text)
                    print(pdf_text)
                    # return {
                    #     'type': 'ir.actions.act_window',
                    #     'view_mode': 'form',
                    #     'res_model': 'clg.student',
                    #     'res_id': self.id,
                    #     'target': 'new',
                    #     'name': 'PDF Content',
                    #     'context': {
                    #         'default_name': 'PDF Content',
                    #         'default_text': pdf_text,
                    #     }
                    # }
                else:
                    raise UserError("PDF file is empty.")
            except PyPDF2.utils.PdfReadError:
                raise UserError("The PDF file appears to be corrupted or incomplete.")
        else:
            raise UserError("No PDF file attached.")

