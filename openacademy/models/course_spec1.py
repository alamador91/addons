from odoo import models, fields

class SpecCourse(models.Model):
    _name = 'oa.course'
    _inherit = "oa.course"
    _description = 'Spec Course'

    attaaaa = fields.Char()
