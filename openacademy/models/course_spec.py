from odoo import models, fields

class SpecCourse(models.Model):
    _name = 'oa.spec.course'
    _inherit = "oa.course"
    _description = 'Spec Course'

    att = fields.Char()
