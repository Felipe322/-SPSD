from django.test import TestCase
from presupuestos.models import Presupuesto
from django.core.exceptions import ValidationError


class TestModels(TestCase):

    def setUp(self):

        self.actividad = Actividad(
            programa='27',
            componente='2',
            actividad='3',
            monto=2982.23,
            descripcion='Presupuesto para Febrero',
            mes='02',
            partida=self.define_partida(),
            anio=self.define_presupuesto()
        )

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

    def test_actividad_model_mes_formato(self):
        self.actividad.save()
        self.actividad.mes = 'Enero'
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()
