from odoo import fields, models
from odoo.fields import Date as d
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "re.estate.property"
    _description = "Estate Property"


    def todayPlus3(self):
        return d.today() + relativedelta(months=3)

    name = fields.Char(required=True, default="Unknown")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=todayPlus3)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean(string="Has garage")
    garden = fields.Boolean(string="Has garden")
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection=[("north", "North"), ("south", "South"), ("west", "West"), ("east", "East")]
    )
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    active = fields.Boolean(default=True)
    state = fields.Selection(
        required=True,
        copy=False,
        selection=[("new", "New"), ("o_received", "Offer Received"), ("o_accepted", "Offer Accepted"), ("sold", "Sold"), ("cancelled", "Canceled")],
        default='new'
    )

