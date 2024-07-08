from odoo import fields, models

class Attendee(models.Model):
    _name = "oa.attendee"
    _inherit = "res.partner"
    #_inherits = {"res.partner": "partner_id"}
    _description = "People attending to sessions"

    #partner_id = fields.Many2one("res.partner")
    sessions = fields.Many2many("oa.session")


    avatar_1920 = fields.Image("Avatar")
    avatar_1024 = fields.Image("Avatar 1024")
    avatar_512 = fields.Image("Avatar 512")
    avatar_256 = fields.Image("Avatar 256")
    avatar_128 = fields.Image("Avatar 128")

    def _compute_avatar(self, avatar_field, image_field):
        pass



