from odoo import fields, models

class TestModel(models.Model):
    _name = "re.test.model"
    _description = 'Test Model'

    name = fields.Char("Nombre de la prueba")
    passed = fields.Boolean("si paso la prueba", default=False)
