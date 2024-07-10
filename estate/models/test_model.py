from odoo import fields, models

class TestModel(models.Model):
    _name = "re.test.model"
    _description = 'Test Model'

    name = fields.Char("Nombre de la prueba")
    passed = fields.Boolean("si paso la prueba", default=False)

    line_ids = fields.One2many("re.test.model.line", "model_id")

class TestModelLine(models.Model):
    _name = "re.test.model.line"
    _description = 'Test Model Line'

    model_id = fields.Many2one("re.test.model")
    f1 = fields.Char()
    f2 = fields.Char()
