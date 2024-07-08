from odoo import models, fields

class Course(models.Model):
    _name = "oa.course"
    _description = "Courses in the platform"

    _rec_name = 'title'

    title = fields.Char(required=True)
    description = fields.Text()
    responsible = fields.Many2one("res.users")
    #students = fields.Many2many("res.partner")
    session_ids = fields.One2many("oa.session", "course", string="Sessions")

