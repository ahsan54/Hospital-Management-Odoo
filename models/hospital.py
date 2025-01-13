from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import timedelta
from odoo.exceptions import UserError


class Hospital(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient Here'

    name = fields.Char(string="Patient", required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender", default='male', tracking=True)
    description = fields.Text("Description Of Disease", default="Enter Here...", required=True)
    patient_disease = fields.Many2one("hospital.doctor", "Disease")
    medicine = fields.Text("Perceived Medicine", required=False)
    dob = fields.Date(string="Date Of Birth")
    patient_age = fields.Integer(string="Age", compute="_compute_patient_age", store=True)
    date_of_last_visit = fields.Date(string="Last Visit")

    @api.depends('dob')
    def _compute_patient_age(self):
        today = fields.Date.today()
        for rec in self:
            if rec.dob:
                age_diff = today.year - rec.dob.year
                rec.patient_age = age_diff
            else:
                rec.patient_age = 0

    @api.constrains('dob')
    def validate_dob(self):
        today = fields.Date.today()
        for rec in self:
            if rec.dob and rec.dob > today:
                raise UserError("Dob should not be grater then today")

    state = fields.Selection(
        [('available', 'Available'), ('lost', 'Lost'), ('draft', 'Draft'), ('cancel', 'Cancelled'), ('done', 'Done')],
        string="State",
        default='draft')

    def action_available(self):
        for x in self:
            x.update({'state': 'available'})

    def action_lost(self):
        for x in self:
            x.update({'state': 'lost'})

    def action_draft(self):
        for x in self:
            x.update({'state': 'draft'})

    def action_done(self):
        for x in self:
            x.update({'state': 'done'})

    def action_cancel(self):
        for x in self:
            x.update({'state': 'cancel'})


    reference_no = fields.Char('Reference No', readonly=True, copy=False, default=lambda self: _('New'))

    @api.model
    def create(self, vals):
        if vals.get('reference_no', _('New')) == _('New'):
            vals['reference_no'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
            print(f"Generated Reference No: {vals['reference_no']}")
        return super(Hospital, self).create(vals)




class Doctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor Information"
    _rec_name = 'doctor_expertise'

    name = fields.Char(string="Name")
    doctor_expertise = fields.Char(string="Expertise")
