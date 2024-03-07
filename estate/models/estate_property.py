# -*- coding: utf-8 -*-

from calendar import c
from odoo import models, fields
from dateutil.relativedelta import relativedelta


def get_default_date(*args):
    return fields.Date.today() + relativedelta(months=3)


class Property(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=get_default_date)
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = (
        fields.Selection(
            string="Garden Orientation",
            selection=[
                ("north", "North"),
                ("south", "South"),
                ("east", "East"),
                ("west", "West"),
            ],
        ),
    )
    state = fields.Selection(
        [
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        required=True,
        copy=False,
        default="new",
    )
    active = fields.Boolean(default=True)
