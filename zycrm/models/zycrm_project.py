from odoo import api, fields, models


class ZyCrmProject(models.Model):
    # _name = 'zycrm.lead'
    _name = "zycrm.project"
    _description = "Zynalog CRM Customer Project"
    
    name = fields.Char(string="Name")
    partner_id = fields.Many2one(
        "res.partner",
        string="Customer",
        check_company=True,
        index=True,
        # tracking=10,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        help="Linked partner (optional). Usually created when converting the lead. You can find a partner by its Name, TIN, Email or Internal Reference.",
    )
    product_id = fields.Many2one("product.template")

    project_name = fields.Char(string="Customer Project")
    project_description = fields.Text(string="Project Description")
    project_market = fields.Char(string="Market")

    peak_annual_units = fields.Integer(string="Customer Peak Annual Units")
    asp = fields.Float(
        "ASP($)",
        #   currency_field='company_currency',
        # tracking=True,
    )
    peak_annual_revenue = fields.Float(
        "Peak Annual Revenue($)",
        # currency_field="company_currency",
        # tracking=True
    )

    @api.depends("peak_annual_units", "asp")
    def _compute_peak_annual_revenue(self):
        for project in self:
            if not project.asp or not project.peak_annual_units:
                project.peak_annual_revenue = 0
            project.peak_annual_revenue = project.asp * project.peak_annual_units
