from odoo import api, fields, models


zy_product_lines = [
    ("1", "ADC"),
    ("2", "REF"),
]

zy_adc_partnumbers = [
    ("1", "ZAD250S12"),
    ("2", "ZAD250D12"),
    ("3", "ZAD250S14"),
    ("4", "ZAD250D14"),
]

class ZyProduct(models.Model):
    # _name = 'zyproduct.zyproduct'
    _inherit = 'product.template'
    name = fields.Char('Product', index=True, required=True, translate=True)
    # detailed_type = fields.Selection([
    # ('adc', 'ADC'),
    # ('ref', 'REF')], 
    # string='Product Line', default='adc', required=True,
    # # help='A storable product is a product for which you manage stock. The Inventory app has to be installed.\n'
    #         # 'A consumable product is a product for which stock is not managed.\n'
    #         # 'A service is a non-material product you provide.'
    # ondelete="cascade",
    # )
    
    productline = fields.Selection(zy_product_lines, string="Product Line")
    partnumber = fields.Char(string="Partnumber")
    
    # productline = fields.Selection(zy_product_lines, string="Product Line")
    # partnumber = fields.Selection(zy_adc_partnumbers, string="Partnumber")
    