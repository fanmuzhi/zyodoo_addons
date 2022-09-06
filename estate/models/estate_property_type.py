from odoo import api, models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate property type description"

    name = fields.Char(string="Name")
