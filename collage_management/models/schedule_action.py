from odoo import models, fields,api,_
from datetime import datetime, timedelta


class SendMailReminder(models.Model):
    _name="send.mail.reminder.admin"
    _description="send mail"
    


    def send_mail_alert(self):
        today = fields.Date.today()
        for student in self.env['mail.activity.schedule'].search([('date_deadline','!=',False)]):
          deadline = student.date_deadline
          if deadline and isinstance(deadline, str):
                deadline = fields.Date.from_string(deadline)

          if isinstance(deadline, fields.Date):
                days_difference = (deadline - today).days
                if days_difference >= 1:
                    admin_email = 'odoobot@example.com'  
                    subject = "Follow-up Reminder"
                    body = f"Dear Admin,\n\nThis is to inform you that the student  has not followed up as of today.\n\nThank you"
                    self.env['mail.mail'].create({
                        'subject': subject,
                        'body_html': body,
                        'email_to': admin_email,
                    }).send()

                       
                   

