from django.test import TestCase
from partidas.forms import Capitulo
from partidas.forms import Partida
from presupuestos.forms import Presupuesto
from presupuestos.forms import Actividad
from presupuestos.forms import ActividadForm


class TestFormActividad(TestCase):

    def setUp(self,
              programa='27',
              componente='2',
              actividad='3',
              monto=2982.23,
              descripcion='Presupuesto para Febrero',
              mes='02',
              ):

        self.actividad = Actividad(
            programa=programa,
            componente=componente,
            actividad=actividad,
            monto=monto,
            descripcion=descripcion,
            mes=mes,
            partida=self.define_partida(),
            anio=self.define_presupuesto()

        )

        self.data = {
            'programa': programa,
            'componente': componente,
            'actividad': actividad,
            'monto': monto,
            'descripcion': descripcion,
            'mes': mes,
            'partida': self.define_partida(),
            'anio': self.define_presupuesto()
        }

    def define_capitulo(self):
        capitulo = Capitulo(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

    def define_partida(self):
        partida = Partida(
            clave=2110,
            nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
            descripcion='Plumas, borradores, entre otras cosas.',
            capitulo=self.define_capitulo()
        )

    def define_presupuesto(self):
        presupuesto = Presupuesto(
            anio='2020',
            fecha='2020-12-3'
        )

    def test_actividad_form_valido(self):  # Err
        form = ActividadForm(self.data)
        self.assertTrue(form.is_valid())

    def test_actividad_form_programa_vacia(self):
        self.data['programa'] = ''
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['programa'],
            ['Este campo es obligatorio.']
        )

    def test_actividad_form_componente_vacia(self):
        self.data['componente'] = ''
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['componente'],
            ['Este campo es obligatorio.']
        )

    def test_actividad_form_actividad_vacia(self):
        self.data['actividad'] = ''
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['actividad'],
            ['Este campo es obligatorio.']
        )

    def test_actividad_form_descripcion_vacia(self):
        self.data['descripcion'] = ''
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['descripcion'],
            ['Este campo es obligatorio.']
        )

    def test_actividad_form_mes_vacia(self):
        self.data['mes'] = ''
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['mes'],
            ['Este campo es obligatorio.']
        )

    def test_actividad_form_partida_vacia(self):
        self.data['partida'] = ''
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['partida'],
            ['Este campo es obligatorio.']
        )

    def test_actividad_form_anio_vacia(self):
        self.data['anio'] = ''
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['anio'],
            ['Este campo es obligatorio.']
        )

    def test_actividad_form_programa_caracteres_mayor(self):
        self.data['programa'] = '123'
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['programa'],
            ['El número de caracteres excede el límite']
        )

    def test_actividad_form_componente_caracteres_mayor(self):
        self.data['componente'] = '123'
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['componente'],
            ['El número de caracteres excede el límite']
        )

    def test_actividad_form_actividad_caracteres_mayor(self):
        self.data['actividad'] = '123'
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['actividad'],
            ['El número de caracteres excede el límite']
        )

    def test_actividad_form_monto_mayor(self):
        self.data['monto'] = 9999999999.99
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['monto'],
            ['El monto rebasa el límite 99999999.99,']

        )

    def test_actividad_form_monto_menor(self):
        self.data['monto'] = 0
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['monto'],
            ['El monto no puede ser menor a 0']

        )

    def test_actividad_form_mes_numero(self):
        self.data['mes'] = 13
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['mes'],
            ['El mes debe ser del 1 a 12']

        )

    def test_actividad_form_descripcion_mayor(self):
        self.data['descripcion'] = 'prueba'*500
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['descripcion'],
            ['La descripción supera 2300 caracteres']

        )
