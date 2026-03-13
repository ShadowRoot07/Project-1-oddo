from odoo import models, fields

class ProductoGamer(models.Model):
    # Heredamos del modelo de productos de Odoo
    _inherit = 'product.template'

    # Añadimos un campo nuevo: ¿Es un producto para Gamers?
    is_gamer = fields.Boolean(string="¿Es para Gamers?", default=False)
    
    # Añadimos un campo de texto para una descripción corta de e-commerce
    web_description = fields.Text(string="Descripción para la web")

