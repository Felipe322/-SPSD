from django.test import TestCase
from presupuestos.models import Presupuesto
from django.core.exceptions import ValidationError



class TestModels(TestCase):

	def setUp(self, anio='2020', fecha='2020-12-01'):

		self.presupuesto = Presupuesto(
			anio=anio,
            fecha=fecha
		)
	
	def test_anio_no_acepta_espacio(self):
		self.presupuesto.anio = '98 0'
		with self.assertRaises(ValidationError):
			self.presupuesto.full_clean()

	def test_anio__no_acepta_caracteres_especiales(self):
		self.presupuesto.anio = '87#4'
		with self.assertRaises(ValidationError):
			self.presupuesto.full_clean()

	def test_fecha_formato(self):
		self.presupuesto.fecha = '2020/12/01'
		with self.assertRaises(ValidationError):
			self.presupuesto.full_clean()

	def test_anio_duplicado(self):
		self.presupuesto.save()
		presupuesto2 = Presupuesto(
			anio='2020',
			fecha ='2020-12-01',
		)
		try:
			presupuesto2.full_clean()
		except ValidationError as ex:
			msg = str(ex.message_dict['anio'][0])
			self.assertEqual(msg, 'A user with that username already exists.')
	