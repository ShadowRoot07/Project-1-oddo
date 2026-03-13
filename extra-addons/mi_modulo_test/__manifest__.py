{
    'name': 'Mi Primer Módulo desde Termux',
    'version': '1.0',
    'author': 'ShadowRoot07',
    'category': 'Tools',
    'summary': 'Módulo de prueba creado desde un móvil usando Termux y NeoVim',
    'depends': ['base', 'product'], # 'product' es necesario para los productos
    'data': [
        'security/ir.model.access.csv',
        'views/producto_view.xml',
        'data/import_productos.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

