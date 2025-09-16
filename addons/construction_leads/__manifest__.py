{
    'name': 'Construction Leads',
    'version': '1.0',
    'summary': 'Module to manage leads for construction projects',
    'description': """
        This module allows managing contact information and follow-up for construction project leads.
    """,
    'author': 'Jules',
    'website': '',
    'category': 'Sales/CRM',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/construction_lead_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
