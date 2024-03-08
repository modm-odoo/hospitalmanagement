#-*- coding: utf-8 -*-

from odoo import http, fields
import random
class Main(http.Controller):

    @http.route(['/doctor'], type="http", auth="public", website=True)
    def display_doctors(self, **kwargs):
        # Fetch doctors from the hospital.doctor model
        Doctor = http.request.env['hospital.doctor']
        doctors = Doctor.search([])  # You may want to add a domain here to filter doctors
        return http.request.render("hospitalMan.index", {
            "doctors": doctors,
        })

    from odoo import http

class DoctorController(http.Controller):

    @http.route('/doctor/<int:doctor_id>', type='http', auth='public', website=True)
    def doctor_details(self, doctor_id, **kwargs):
        Doctor = http.request.env['hospital.doctor']
        doctor = Doctor.browse(doctor_id)
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        
        while b <= a:
            a = random.randint(0, 9)
            b = random.randint(0, 9)
        random1 = [a, b]

        return http.request.render("hospitalMan.doctor_details_template", {
            "doctor": doctor,
            "random": random1,
        })
