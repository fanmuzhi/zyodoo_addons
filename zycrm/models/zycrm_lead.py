from odoo import api, fields, models


markets = [
    ("automobile", "Automobile"),
    ("electronics", "Electronics"),
    ("telecommunication", "Telecommunication"),
    ("medical", "Medical"),
    ("industrial", "Industrial"),
    ("instrument", "Instrument"),
    ("others", "Others"),
]

class ZyLead(models.Model):
    # _name = 'zycrm.lead'
    _inherit = 'crm.lead'
    
    product_id = fields.Many2one("product.template", string="Product", required=True)
    productline = fields.Selection(related="product_id.productline", readonly=True)
    partnumber = fields.Char(related="product_id.partnumber", readonly=True)

    project_name = fields.Char(string="Project", required=True)
    project_description = fields.Text(string="Project Description", required=True)
    project_market = fields.Selection(markets, string="Market", required=True)
    asp = fields.Monetary('ASP($)', currency_field='company_currency', tracking=True)
    peak_annual_units = fields.Integer(string="Peak Annual Units")
    peak_annual_revenue = fields.Monetary('Peak Annual Revenue($)', currency_field='company_currency', tracking=True, compute="_compute_peak_annual_revenue")
    competitor = fields.Char(string="Competitor")
    
    # project_id = fields.Many2one("zycrm.project")
    # project_name = fields.Char(string='Project Name', related="project_id.project_name")
    # project_description = fields.Text(string='Project Description', related="project_id.project_description")
    # project_market = fields.Char(string="Market", related="project_id.project_market")
    
    # peak_annual_units = fields.Integer(string="Customer Peak Annual Units", related="project_id.peak_annual_units")
    # asp = fields.Float('ASP($)', related="project_id.asp")
    # peak_annual_revenue = fields.Float('Peak Annual Revenue($)', related="project_id.peak_annual_revenue", readonly=True)
    
    # state_id = fields.Many2one(
    # "res.country.state", string='Province',
    # compute='_compute_partner_address_values', readonly=False, store=True,
    # domain="[('country_id', '=?', country_id)]")
    
    user_id = fields.Many2one(
    'res.users', string='Disti Sales', default=lambda self: self.env.user,
    domain="['&', ('share', '=', False), ('company_ids', 'in', user_company_ids)]",
    check_company=True, index=True, tracking=True)
    
    team_id = fields.Many2one(
    'crm.team', string='Disti', check_company=True, index=True, tracking=True,
    domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
    compute='_compute_team_id', ondelete="set null", readonly=False, store=True)
    
    # @api.depends("partner_id", "product_id")
    # def _compute_project_partner_id(self):
    #     for lead in self:
    #         lead.project_id.partner_id = lead.partner_id
    #         lead.project_id.product_id = lead.product_id
    
    @api.depends("peak_annual_units", "asp")
    def _compute_peak_annual_revenue(self):
        for lead in self:
            if not lead.asp or not lead.peak_annual_units:
                lead.peak_annual_revenue = 0
            else:
                lead.peak_annual_revenue = lead.asp * lead.peak_annual_units

            
    

