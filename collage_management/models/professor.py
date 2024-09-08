from odoo import fields,models,api

class professor(models.Model):
    _name = 'clg.professor'
    _description = 'Professor'
   
    namee=fields.Char(string="Name")
    subject=fields.Char(string="subject")
   
    student_lines_ids = fields.One2many('clg.studentlines', 'student_id' ,string="Student List")

    # @api.onchange('student_id')
    # def onchange_name(self):
    #     if self.student_id:
    #         self.collage=self.student_id.collage
    #         self.mono=self.student_id.mono

    def button_approved(self):
        student_obj = self.env['clg.student']
        for professor in self:
            for student_line in professor.student_lines_ids:
                student = student_line.name
                if student:
                    student.write({'namee': [(4, professor.id)]})

        return True

class studentlines(models.Model):
    _name='clg.studentlines'
    _description="student lines"


    name=fields.Many2one("clg.student" ,string='Student Name:')
    collage=fields.Char()
    mono=fields.Char()

    student_id = fields.Many2one('clg.professor', string="Student ID")

    @api.onchange('name')
    def onchange_name(self):
        if self.name:
            self.collage=self.name.collage.collagename
            self.mono=self.name.mono
