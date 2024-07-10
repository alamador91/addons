from odoo import api, exceptions, fields, models
from odoo.fields import Date as d
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "re.estate.property"
    _description = "Estate Property"
    _order = "id DESC"


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
        default="new",
        compute="_compute_state",
        store=True,
    )

    property_type_id = fields.Many2one("re.estate.property.type")
    buyer_id = fields.Many2one("res.partner", copy=False)
    seller_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    property_tag_ids = fields.Many2many("re.estate.property.tag")
    offer_ids = fields.One2many("re.estate.property.offer", "property_id", string="Offers")

    total_area = fields.Float(compute="_compute_total_area", string="Total Area (sqm)", readonly=True)
    best_offer = fields.Float(compute="_compute_best_offer", string="Best Offer", readonly=True)

    _sql_constraints = [
        ("name_uniq", "UNIQUE(name)", "The name of the property must be unique"),
        ("prop_unique", "UNIQUE(name, property_type_id)", "The property name and type must be unique"),
        #("positive_price", "CHECK(expected_price >= 0)", "The expected price must be positive"),
        #("positive_s_price", "CHECK(selling_price >= 0)", "The selling price must be positive"),
        ("positive_area", "CHECK(living_area >= 0)", "The living area must be positive"),
        #("positive_garden_area", "CHECK(garden_area >= 0)", "The garden area must be positive"),
    ]

    @api.depends('offer_ids')
    def _compute_state(self):
        for record in self:
            if len(record.offer_ids) != 0 and record.state == "new":
                record.state = "o_received"

    @api.depends('garden_area', 'living_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.garden_area + record.living_area

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for record in self:
            if len(record.offer_ids) == 0:
                record.best_offer = 0
            else:
                record.best_offer = max(record.offer_ids.mapped('price'))
            # bp = record.best_offer
            # for of in record.offer_ids:
            #     if of.price > bp:
            #         bp = of.price
            # record.best_offer = bp

        #return {'warning': {
        #    'title': ("Warning"),
        #    'message': ('This option is not supported for Authorize.net')}}

    @api.onchange("garden")
    def _onchange_has_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = None
            self.garden_orientation = None

    def action_sale(self):
        self.ensure_one()
        if self.state == "cancelled":
            raise exceptions.UserError('U cant sell a cancelled property')
        self.state = "sold"


    def action_cancel(self):
        self.ensure_one()
        if self.state == "sold":
            raise exceptions.UserError('U cant cancel a sold property')
        self.state = "cancelled"

    #@api.constrains('offer_ids')
    #def _check_90_percent(self):
    #    for record in self:
    #        if record.offer_ids.price < record.expected_price * 0.9:
    #            raise exceptions.ValidationError('The offer price is less than 90% of the expected price')

    @api.constrains('selling_price')
    def _check_90_percent(self):
        for record in self:
            #if record.state not in ["o_accepted", "sold"]:
            #    record.selling_price = 0
            #    return
            if record.state == "new":
                return
            if record.selling_price < record.expected_price * 0.9:
                raise exceptions.ValidationError('The selling price is less than 90% of the expected price')
