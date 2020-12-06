from django.test import TestCase
from partidas.forms import Partida
from partidas.forms import Capitulo
from django.core.exceptions import ValidationError


class TestModelsPartida(TestCase):

    def setUp(self,
              clave=2110,
              nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
              descripcion='Plumas, borradores, entre otras cosas.'
              ):

        self.admin_login()

        self.capitulo = Capitulo.objects.create(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

        self.partida = Partida.objects.create(
            clave=clave,
            nombre=nombre,
            descripcion=descripcion,
            capitulo=self.capitulo
        )

        self.data = {
            'clave': clave,
            'nombre': nombre,
            'descripcion': descripcion,
            'capitulo': self.capitulo
        }

    def test_partida_duplicado(self):
        partida_repetido = Partida(
            clave=2210,
            nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
            descripcion='Plumas, borradores, entre otras cosas.',
            capitulo=Capitulo(
                clave=2000,
                nombre='MATERIALES Y SUMINISTROS'
            )
        )
        try:
            partida_repetido.full_clean()
        except ValidationError as ex:
            msg = str(ex.message_dict['clave'][0])
            self.assertEqual(
                msg,
                'Ya existe un/a partida con este/a Clave.')

    def test_partida_clave_minimo_caracteres(self):
        self.partida.clave = 18
        with self.assertRaises(ValidationError):
            self.partida.full_clean()
