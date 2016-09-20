# -*- coding: utf-8 -*-
from datetime import datetime
from dateutil import relativedelta
from openerp import models, fields, api

class hr_employee(models.Model):
	_inherit = 'hr.employee'

	employee_number = fields.Char('Nomor Induk Karyawan (NIK)')
	tanggal_masuk = fields.Date('Tanggal Masuk')
	golongan_id = fields.Many2one('hr.golongan','Golongan')
	pendidikan_id = fields.Many2one('hr.pendidikan','Pendidikan')
	gaji_pokok = fields.Float('Gaji Pokok')
	lama_bekerja = fields.Char('Lama Bekerja', compute="_lama_bekerja")

	@api.one
	@api.depends('tanggal_masuk')
	def _lama_bekerja(self):
		if self.tanggal_masuk:
			tanggal_masuk = datetime.strptime(str(self.tanggal_masuk), '%Y-%m-%d')
			total_time = relativedelta.relativedelta(datetime.now(),tanggal_masuk)
			if total_time.years > 0:
				self.lama_bekerja = "%s Tahun %s Bulan" %(total_time.years,total_time.months)
			else:
				self.lama_bekerja = "%s Bulan" %(total_time.months)
		else:
			self.lama_bekerja = "-"

class hr_department(models.Model):
	_inherit = 'hr.department'

	layanan_ids = fields.One2many('hr.department.layanan','department_id','Layanan')

class hr_golongan(models.Model):
	_name = 'hr.golongan'
	_description = 'Golongan Karyawan'
	_inherit = ['mail.thread', 'ir.needaction_mixin']

	name = fields.Char('Golongan')
	member_ids = fields.One2many('hr.employee','golongan_id', 'Members', readonly=True)
	color = fields.Integer('Color Index')
	skor = fields.Integer('Skor')

class hr_pendidikan(models.Model):
	_name = 'hr.pendidikan'
	_description = 'Pendidikan Karyawan'
	_inherit = ['mail.thread', 'ir.needaction_mixin']

	name = fields.Char('Pendidikan Terakhir')
	member_ids = fields.One2many('hr.employee','pendidikan_id', 'Members', readonly=True)
	color = fields.Integer('Color Index')
	skor = fields.Integer('Skor')
	keterangan = fields.Html('Keterangan')

class hr_department_layanan(models.Model):
	_name = 'hr.department.layanan'
	_description = 'Layanan dalam Unit'
	_inherit = ['mail.thread', 'ir.needaction_mixin']

	name = fields.Char('Nama Layanan')
	department_id = fields.Many2one('hr.department','Unit')
	potongan = fields.Float('Potongan Jasa')