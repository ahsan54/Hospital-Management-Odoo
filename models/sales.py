from odoo import fields, models
from odoo.exceptions import ValidationError
from datetime import timedelta


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_description = fields.Char(string="Sale Description", required=False)


class ExtendingHospital(models.Model):
    _inherit = 'hospital.patient'

    patient_address = fields.Char(string="Address", required=False,default="City-Sate-Country")


