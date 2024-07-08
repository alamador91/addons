from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = "re.estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char(required=True)
