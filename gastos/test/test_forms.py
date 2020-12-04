from django.test import TestCase
from partidas.forms import Capitulo
from partidas.forms import Partida
from presupuestos.forms import Presupuesto
from presupuestos.forms import Actividad
from gastos.forms import GastoForm
from gastos.forms import Gasto


class TestFormGasto(TestCase):

    def setUp(self, descripcion='Se compraron muchos lapízes', proveedor='La comer S.A C.V', precio_unitario=2.50,cantidad=300,fecha='12/12/2020'):

        self.gasto = Gasto(
            descripcion=descripcion,
            proveedor=proveedor,
            precio_unitario=precio_unitario,
            cantidad=cantidad,
            precio_total=precio_unitario*cantidad,
            fecha=fecha,
            id_actividad= self.define_actividad()
        )

        self.data = {
            'descripcion': descripcion,
            'proveedor': proveedor,
            'precio_unitario': precio_unitario,
            'cantidad': cantidad,
            'precio_total': precio_unitario*cantidad,
            'fecha': fecha,
            'id_actividad': self.define_actividad()
        }

    # def test_gasto_form_valido(self): # Err
    #     form = GastoForm(self.data)
    #     self.assertTrue(form.is_valid())

    def test_gasto_form_descripcion_vacia(self):
        self.data['descripcion'] = ''
        form = GastoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_gasto_form_proveedor_vacio(self):
        self.data['proveedor'] = ''
        form = GastoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_gasto_form_precio_unitario_vacio(self):
        self.data['precio_unitario'] = ''
        form = GastoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_gasto_form_cantidad_vacio(self):
        self.data['cantidad'] = ''
        form = GastoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_gasto_form_fecha_vacio(self):
        self.data['fecha'] = ''
        form = GastoForm(self.data)
        self.assertFalse(form.is_valid())

    def test_gasto_form_id_actividad_vacio(self):
        self.data['id_actividad'] = ''
        form = GastoForm(self.data)
        self.assertFalse(form.is_valid())


    #Definición de campos necesarios para crear un Gasto.
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
            fecha='01/12/2020'
        )

    def define_actividad(self):
        actividad = Actividad(
            programa= '27',
            componente= '2',
            actividad= '3',
            monto= 2982.23,
            descripcion= 'Presupuesto para Febrero',
            mes= '02',
            partida= self.define_partida(),
            anio= self.define_presupuesto()
        )

