from odoo import api, models, fields


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "estate property tag model description"

    name = fields.Char(string="Name")
