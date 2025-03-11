# -*- coding: utf-8 -*-
{
    'name': 'I Like Trains',
    'version': '1.0',
    'category': 'Human Resources/Expenses',
    'summary': 'Gestión de billetes de tren para empleados',
    'description': """
        Módulo para gestionar los billetes de tren de los empleados.
    """,
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/train_provider_views.xml',
        'views/train_payment_views.xml',
        'views/train_ticket_views.xml',
        'views/train_route_views.xml',
        'views/train_station_views.xml',
        'views/report_train_ticket.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
