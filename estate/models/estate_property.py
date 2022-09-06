from select import select
from xmlrpc.client import DateTime
from odoo import models, fields


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "real estate ads model"

    name = fields.Char(string="Title")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price")
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden_area")
    garden_orientation = fields.Selection(
        [("North", "North"), ("South", "South"), ("East", "East"), ("West", "West")],
        string="Garden Orientation",
    )
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    saleman = fields.Many2one("res.users", string="Sales")
    buyer = fields.Many2one("res.partner", string="Customer")
    property_type_id = fields.Many2one(
        "estate.property.type", string="Estate Property Type"
    )
    tag_ids = fields.Many2many(
        "estate.property.tag",
        "estate_property_estate_property_tag_rel",
        "estate_property_id",
        "estate_property_tag_id",
        string="Tag",
    )
