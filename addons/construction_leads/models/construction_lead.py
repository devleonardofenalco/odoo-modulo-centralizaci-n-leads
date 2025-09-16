# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ConstructionLead(models.Model):
    _name = 'construction.lead'
    _description = 'Construction Lead'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    phone_number = fields.Char(string='Número de teléfono')
    email = fields.Char(string='Correo electrónico')
    cedula_number = fields.Char(string='Número de cédula')

    preferred_contact_method = fields.Selection([
        ('phone', 'Teléfono'),
        ('mail', 'Mail'),
        ('whatsapp', 'Whatsapp')
    ], string='Medio de contacto preferido')

    lead_origin = fields.Selection([
        ('web', 'Página Web'),
        ('google', 'Google'),
        ('facebook', 'Facebook')
    ], string='Origen Lead')

    customer_note = fields.Text(string='Nota de cliente')

    # Profiling Form Fields
    project_of_interest = fields.Char(string='Proyecto de interés')
    salary_range = fields.Char(string='Rango salarial o salario')
    contract_type = fields.Char(string='Tipo de contrato')
