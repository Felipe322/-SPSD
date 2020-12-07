from django.test import TestCase
from presupuestos.models import Presupuesto
from django.core.exceptions import ValidationError
from presupuestos.models import (Actividad, Presupuesto)
from partidas.models import (Partida, Capitulo)
from django.contrib.auth.models import User


class TestModels(TestCase):

    def setUp(self,
              programa='27',
              componente='2',
              actividad='3',
              monto=2982.23,
              descripcion='Presupuesto para Febrero',
              mes='02',
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

    def test_actividad_model_mes_formato(self):
        self.actividad.save()
        self.actividad.mes = 'Enero'
        with self.assertRaises(ValidationError):
            self.actividad.full_clean()

    def admin_login(self):
        user1 = User.objects.create_user(
            username='admin',
            password='Adri4na203#',
            is_superuser=True
        )
        self.client.login(username='admin', password='Adri4na203#')
