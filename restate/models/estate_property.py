from odoo import models, fields

class RealEstate(models.Model):
    _name="estate.property"
    _description="Description of properties"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [('N', 'North'), ('S', 'South'), ('W', 'West'), ('E', 'East')],
        help = 'Selection of the garden orientation'
    )