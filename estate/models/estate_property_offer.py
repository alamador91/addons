from odoo import api, fields, models
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = "re.estate.property.offer"
    _description = "Estate Property Offer"
    _order = "price DESC"

    price = fields.Float(required=True)
    status = fields.Selection([
        ("accepted", "Accepted"),
        ("refused", "Refused")
    ], string="Status", copy=False, readonly=True)
    property_id = fields.Many2one("re.estate.property", string="Property", required=True)
    partner_id = fields.Many2one("res.partner", string="Partner", required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", string="Deadline", inverse="_inverse_date_deadline", readonly=False)

    _sql_constraints = [
        ("check_validity", "CHECK(validity > 0)", "The validity must be positive"),
        ("positive_offer", "CHECK(price >= 0)", "The price must be positive"),
    ]

    property_type_id = fields.Many2one('re.estate.property.type', related="property_id.property_type_id", store=True)


    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            if record.create_date:
                record.date_deadline = record.create_date + relativedelta(days=record.validity)
            else:
                record.date_deadline = fields.Date.today() + relativedelta(days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - record.create_date.date()).days

    def action_accept(self):
        self.ensure_one()
        self.property_id.selling_price = self.price
        self.status = "accepted"
        self.property_id.buyer_id = self.partner_id.id
        for of in self.property_id.offer_ids:
            if of.id != self.id:
                of.status = "refused"
        self.property_id.state = "o_accepted"

    def action_refuse(self):
        self.ensure_one()
        if self.property_id.state == "sold":
            raise ValidationError("You cant modify a sold property")
        if self.status == "accepted" and self.property_id.state == "o_accepted":
            self.property_id.state = "new"
            self.property_id.selling_price = 0
            self.property_id.state = "o_received"
        self.status = "refused"
