from odoo import fields, models

class Users(models.Model):
    _inherit = 'res.users'

    property_ids = fields.One2many("re.estate.property", "seller_id",
                                   domain=[('state', 'in', ['new', 'o_received'])])
