from odoo import models, fields

class DelCourse(models.Model):
    _name = 'oa.course.del'
    _inherits = {"oa.course": "course_id"}
    _description = 'Spec Delegated'
    _rec_name = 'title'

    course_id = fields.Many2one('oa.course', required=True, ondelete='cascade')
    grade = fields.Char()

