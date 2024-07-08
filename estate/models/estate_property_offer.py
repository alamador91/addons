from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class EstatePropertyOffer(models.Model):
    _name = 're.estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float(required=True)
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Status', copy=False)
    property_id = fields.Many2one('re.estate.property', string='Property', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute='_compute_date_deadline', string='Deadline', inverse="_inverse_date_deadline", readonly=False)


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
        self.status = 'accepted'
        self.property_id.buyer_id = self.partner_id.id
        self.property_id.selling_price = self.price
        for of in self.property_id.offer_ids:
            if of.id != self.id:
                of.status = 'refused'
        self.property_id.state = "sold"

    def action_refuse(self):
        self.ensure_one()
        self.status = 'refused'
