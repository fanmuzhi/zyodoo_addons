{
    'name': 'ZynalogCRM',
    'version': '1.0',
    'summary': 'Zynalog Customized CRM',
    'sequence': 10,
    'description': """
        real estate property demo
    """,
    'depends': ['crm', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/zycrm_views.xml'
    ],
    'demo': [],
    'application': False,
    # 'auto_install': False,
    'license': 'LGPL-3',
}