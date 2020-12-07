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
              mes='02'
              ):
        self.admin_login()

        self.capitulo = Capitulo.objects.create(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

        self.partida = Partida.objects.create(
            clave=2110,
            nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
            descripcion='Plumas, borradores, entre otras cosas.',
            capitulo=self.capitulo
        )

        self.presupuesto = Presupuesto.objects.create(
            anio='2020',
            fecha='2020-12-01'
        )

        self.actividad = Actividad.objects.create(
            programa=programa,
            componente=componente,
            actividad=actividad,
            monto=monto,
            descripcion=descripcion,
            mes=mes,
            partida=self.partida,
            anio=self.presupuesto

        )

        self.actividadDos = Actividad.objects.create(
            programa=programa,
            componente=componente,
            actividad=actividad,
            monto=monto,
            descripcion=descripcion,
            mes=mes,
            partida=self.partida,
            anio=self.presupuesto

        )

        self.data = {
            'programa': programa,
            'componente': componente,
            'actividad': actividad,
            'monto': monto,
            'descripcion': descripcion,
            'mes': mes,
            'partida': self.partida,
            'anio': self.presupuesto
        }

    # def test_actividad_form_valido(self):
    #     form = ActividadForm()
    #     self.assertTrue(form.is_valid())

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
            ['Asegúrese de que este valor tenga menos de 2 caracteres (tiene 3).']
        )

    def test_actividad_form_componente_caracteres_mayor(self):
        self.data['componente'] = '123'
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['componente'],
            ['Asegúrese de que este valor tenga menos de 2 caracteres (tiene 3).']
        )

    def test_actividad_form_mes_numero(self):
        self.data['mes'] = 13
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['mes'],
            ['Ingrese un mes válido']
        )

    def test_actividad_form_descripcion_mayor(self):
        self.data['descripcion'] = 'prueba'*500
        form = ActividadForm(self.data)
        self.assertEqual(
            form.errors['descripcion'],
            ['Asegúrese de que este valor tenga menos de 2300 caracteres (tiene 3000).']
        )

    def admin_login(self):
        self.client.login(username='admin', password='Adri4na203#')
