# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
import json

class ConstructionLeadController(http.Controller):

    @http.route('/api/construction_lead', type='json', auth='public', methods=['POST'], csrf=False)
    def create_lead(self, **kwargs):
        """
        Endpoint to create a new construction lead from a JSON payload.
        Example Payload:
        {
            "name": "John Doe",
            "phone_number": "1234567890",
            "email": "john.doe@example.com",
            "cedula_number": "123456789",
            "preferred_contact_method": "mail",
            "lead_origin": "web",
            "customer_note": "Interested in the new apartment complex.",
            "project_of_interest": "Apartment Complex 'The Heights'",
            "salary_range": "50k-60k",
            "contract_type": "Permanent"
        }
        """
        data = request.jsonrequest

        try:
            lead = request.env['construction.lead'].sudo().create({
                'name': data.get('name'),
                'phone_number': data.get('phone_number'),
                'email': data.get('email'),
                'cedula_number': data.get('cedula_number'),
                'preferred_contact_method': data.get('preferred_contact_method'),
                'lead_origin': data.get('lead_origin'),
                'customer_note': data.get('customer_note'),
                'project_of_interest': data.get('project_of_interest'),
                'salary_range': data.get('salary_range'),
                'contract_type': data.get('contract_type'),
            })
            return {
                'status': 'success',
                'lead_id': lead.id
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }
