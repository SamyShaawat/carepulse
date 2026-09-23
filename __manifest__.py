{
    'name': 'CarePulse',
    'version': '19.0.1.0.0',
    'category': 'Services',
    'summary': 'Clinic management: visit to paid invoice',
    'license': 'Other OSI approved licence',
    'depends': [
        'contacts',
        'crm',
        'calendar',
        'website',
        'sale_management',
        'account',
        'stock',
        'hr',
        'hr_attendance',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}
