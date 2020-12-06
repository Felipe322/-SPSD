from django.test import TestCase
from partidas.forms import PartidaForm
from partidas.forms import Partida
from partidas.forms import Capitulo


class TestFormPartida(TestCase):

    def setUp(self, clave=2110, nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES\
                DE OFICINA', descripcion='Plumas, borradores, entre otras\
                    cosas.'):
        capitulo = Capitulo.objects.create(
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

    def test_partida_form_valido(self):
        form = PartidaForm(self.data)
        self.assertTrue(form.is_valid())

    def test_partida_form_clave_vacio(self):
        self.data['clave'] = ''
        form = PartidaForm(self.data)
        self.assertEqual(
            form.errors['clave'],
            ['Este campo es obligatorio.'])

    def test_partida_form_nombre_vacio(self):
        self.data['nombre'] = ''
        form = PartidaForm(self.data)
        self.assertEqual(
            form.errors['nombre'],
            ['Este campo es obligatorio.'])

    def test_partida_form_descripcion_vacio(self):
        self.data['descripcion'] = ''
        form = PartidaForm(self.data)
        self.assertEqual(
            form.errors['descripcion'],
            ['Este campo es obligatorio.'])

    def test_partida_form_capitulo_vacio(self):
        self.data['capitulo'] = ''
        form = PartidaForm(self.data)
        self.assertEqual(
            form.errors['capitulo'],
            ['Este campo es obligatorio.'])

    def test_partida_form_clave_numero_caracteres_correcta(self):
        self.data['clave'] = 2115
        form = PartidaForm(self.data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_partida_form_clave_numero_caracteres_mayor(self):
        self.data['clave'] = 200003
        form = PartidaForm(self.data)
        self.assertEqual(
            form.errors['clave'],
            ['Asegúrese de que este valor sea menor o igual a 9000.'])

    def test_partida_form_nombre_caracteres_mayor(self):
        self.data['nombre'] = 'MATERIALES Y ÚTILES'*5
        form = PartidaForm(self.data)
        self.assertEqual(
            form.errors['nombre'],
            ['Asegúrese de que este valor tenga menos de \
             75 caracteres (tiene 95).'])

    def test_partida_form_descripcion_caracteres_mayor(self):
        self.data['descripcion'] = 'Plumas, borradores y más.'*10
        form = PartidaForm(self.data)
        self.assertEqual(
            form.errors['descripcion'],
            ['El número de caracteres de la descripción excede el límite.'])

    def test_partida_form_clave_caracteres_numero(self):
        self.data['clave'] = 2200
        form = PartidaForm(self.data)
        self.assertIsInstance(self.data['clave'], int)

    def test_partida_form_clave_repetida(self):
        self.data['clave'] = 2110
        form = PartidaForm(self.data)
        self.assertEqual(
            form.errors['clave'],
            ['La clave ya existe.'])
