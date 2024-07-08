from odoo import models, fields

class Session(models.Model):
    _name = "oa.session"
    _description = "Sessions of each course in the platform"
    _rec_name = "name"

    name = fields.Char()
    start_date = fields.Date()
    duration = fields.Integer()
    number_of_seats = fields.Integer()
    instructor = fields.Many2one("res.partner")
    course = fields.Many2one("oa.course")
    attendees = fields.Many2many("oa.attendee")
