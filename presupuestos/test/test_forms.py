from django.test import TestCase
from presupuestos.forms import PresupuestoForm
from presupuestos.models import Presupuesto


class TestFormPresupuesto(TestCase):

    def setUp(self, anio='2020', fecha='2020-12-1'):
        self.presupuesto = Presupuesto.objects.create(
            anio=anio,
            fecha=fecha
        )

        self.data = {
            'anio': anio,
            'fecha': fecha
        }

    def test_presupuesto_form_valido(self):
        self.data['anio'] = 2021
        form = PresupuestoForm(self.data)
        self.assertTrue(form.is_valid())

    def test_presupuesto_form_anio_vacio(self):
        self.data['anio'] = ''
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['anio'],
            ['Este campo es obligatorio.'])

    def test_presupuesto_form_fecha_vacio(self):
        self.data['fecha'] = ''
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['fecha'],
            ['Este campo es obligatorio.'])

    def test_presupuesto_form_anio_numero_caracteres_correcta(self):
        self.data['anio'] = 1928
        form = PresupuestoForm(self.data)
        self.assertTrue(form.is_valid())

    def test_presupuestos_form_anio_numero_caracteres_mayor(self):
        self.data['anio'] = 20090
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['anio'],
            ['Asegúrese de que este valor tenga menos de 4 caracteres (tiene 5).'])

    def test_presupuestos_form_anio_numero_caracteres_menor(self):
        self.data['anio'] = 891
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['anio'],
            ['Ingrese un año válido'])

    def test_presupuestos_form_anio_caracteres_solo_numeros(self):
        self.data['anio'] = 'aaaa'
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['anio'],
            ['Ingrese un año válido'])

    def test_presupuestos_form_fecha_no_valida(self):
        self.data['fecha'] = '1010-88-1'
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['fecha'],
            ['Introduzca una fecha válida.'])

    def test_presupuestos_form_fecha_valida(self):
        self.data['anio'] = 2021
        self.data['fecha'] = '2020-03-12'
        form = PresupuestoForm(self.data)
        self.assertTrue(form.is_valid())
