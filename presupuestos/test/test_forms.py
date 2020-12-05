from django.test import TestCase
from presupuestos.forms import PresupuestoForm
from presupuestos.models import Presupuesto


class TestFormPresupuesto(TestCase):

    def setUp(self, anio='2020', fecha='2020-12-1'):
        self.presupuesto = Presupuesto(
            anio=anio,
            fecha=fecha
        )

        self.data = {
            'anio': anio,
            'fecha': fecha
        }

    
    def test_presupuesto_form_valido(self):
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
            ['El número de caracteres del año es mayor que 4'])
    

    
    def test_presupuestos_form_anio_numero_caracteres_menor(self):
        self.data['anio'] = 891
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['anio'],
            ['El número de caracteres del año es menor que 4'])
    

    
    def test_presupuestos_form_anio_caracteres_solo_numeros(self):
        self.data['anio'] = 'aaaa'
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['anio'],
            ['El campo año solo permite caracteres numericos'])
    

    
    def test_presupuestos_form_fecha_no_valida(self):
        self.data['fecha'] = '1010-88-1'
        form = PresupuestoForm(self.data)
        self.assertEqual(
            form.errors['fecha'],
            ['Introduzca una fecha válida.'])

    def test_presupuestos_form_fecha_valida(self):
        self.data['fecha'] = '2020-03-12'
        form = PresupuestoForm(self.data)
        self.assertTrue(form.is_valid())
    

