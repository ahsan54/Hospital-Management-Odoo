{
    'name': 'patient',  # Module name
    'author': 'Ahsan',  # author name
    'description': "This is Lahore Central hospital patients",  # desc about app
    'version': '1.0',  # specify version of app after odoo
    'summary': 'This is 5_Agust Lahore Central patients',  # give little info about app
    'sequence': 1,  # set the position in all apps
    'category': 'Lahore Central patients',  # will displayed in info
    'website': 'https://www.google.com',  # will displayed in info
    'depends': ['base','sale','mail'],  # those modules , on which our app depends , inheriot them here
    'installable': True,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patinet.xml',
        'views/sale.xml',
        'views/doctor.xml',
        'views/appointment.xml',
    ]
}
