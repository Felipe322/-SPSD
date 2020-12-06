from django.test import TestCase
from partidas.forms import Capitulo
from partidas.forms import Partida
from presupuestos.forms import Presupuesto
from presupuestos.forms import Actividad
from gastos.forms import Gasto
from django.core.exceptions import ValidationError


class TestModelsGasto(TestCase):

    def setUp(self, descripcion='Se compraron muchos lapízes',
              proveedor='La comer S.A C.V', precio_unitario=2.50,
              cantidad=300, fecha='2020-12-12'):

        self.gasto = Gasto(
            descripcion=descripcion,
            proveedor=proveedor,
            precio_unitario=precio_unitario,
            cantidad=cantidad,
            precio_total=precio_unitario*cantidad,
            fecha=fecha,
            id_actividad=self.define_actividad()
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

    def test_fecha_formato(self):
        self.gasto.fecha = '2020/12/01'
        with self.assertRaises(ValidationError):
            self.gasto.full_clean()

    # Definición de campos necesarios para crear un Gasto.
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
            fecha='2020-12-01'
        )

    def define_actividad(self):
        actividad = Actividad(
            programa='27',
            componente='2',
            actividad='3',
            monto=2982.23,
            descripcion='Presupuesto para Febrero',
            mes='02',
            partida=self.define_partida(),
            anio=self.define_presupuesto()
        )
