from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta
from odoo.exceptions import UserError


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'This handles the appointments of patients'

    def default_date(self):
        return fields.Date.today()

    patient_id = fields.Many2one('hospital.patient',required=True,copy=True,readonly=False,)
    date_appointment = fields.Date('Appointment Date',default=lambda X : X.default_date())
    age = fields.Integer('Age',tracking=True)

