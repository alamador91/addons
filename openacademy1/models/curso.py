from odoo import models, fields

class Curso(models.Model):
    _name='oa.curso'
    _description='Los cursos que se van a dar en la academia'

    name=fields.Char()
    edition=fields.Integer()