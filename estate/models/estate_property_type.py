from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = "re.estate.property.type"
    _description = "Estate Property Type"
    _order = "name"

    name = fields.Char(required=True)
    sequence = fields.Integer(default=1)

    property_ids = fields.One2many("re.estate.property", "property_type_id", string="Properties")

    offer_ids = fields.One2many("re.estate.property.offer", "property_type_id")
    offer_count = fields.Integer(compute="_compute_offer_count")

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)
