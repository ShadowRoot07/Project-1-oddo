from odoo import models, fields

class GamerSetup(models.Model):
    _name = 'gamer.setup'
    _description = 'Configuración Gamer'

    name = fields.Char(string="Nombre del Setup", required=True)
    cpu = fields.Char(string="Procesador")
    gpu = fields.Char(string="Tarjeta Gráfica")
    has_rgb = fields.Boolean(string="¿Tiene RGB?", default=True)

