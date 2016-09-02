# -*- coding: utf-8 -*-
{
    'name': "hr_remunerasi",
    'summary': """
        Remunerasi dokter untuk rumah sakit umum daerah
        RSUD Embung Fatimah Batam""",
    'description': """
        Perhitungan pembagian insentive pegawai rumah sakit
    """,
    'author': "Rachmat Aditiya",
    'website': "http://radit.haragreen.com",
    'category': 'Human Resource',
    'version': '9.0.0.1',
    'depends': ['base_setup','mail','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_remunerasi.xml',
        'views/hr_employee.xml',
        'views/hr_dashboard.xml',
    ],
}