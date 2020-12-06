from django.test import TestCase
from partidas.forms import CapituloForm
from partidas.forms import Capitulo


class TestFormCapitulo(TestCase):

    def setUp(self, clave=2001, nombre='MATERIALES Y SUMINISTROS 2'):
        self.capitulo = Capitulo.objects.create(
            clave=4001,
            nombre='MATERIALES Y SUMINISTROS'
        )

        self.data = {
            'clave': 4001,
            'nombre': 'MATERIALES Y SUMINISTROS'
        }

    def test_capitulo_form_valido(self):
        self.data['clave'] = 3000
        form = CapituloForm(self.data)
        self.assertTrue(form.is_valid())

    def test_capitulo_form_clave_vacio(self):
        self.data['clave'] = ''
        form = CapituloForm(self.data)
        self.assertEqual(
            form.errors['clave'],
            ['Este campo es obligatorio.'])

    def test_capitulo_form_nombre_vacio(self):
        self.data['nombre'] = ''
        form = CapituloForm(self.data)
        self.assertEqual(
            form.errors['nombre'],
            ['Este campo es obligatorio.'])

    def test_capitulo_form_clave_numero_caracteres_correcta(self):
        self.data['clave'] = 1000
        form = CapituloForm(self.data)
        self.assertTrue(form.is_valid())

    def test_capitulo_form_clave_numero_caracteres_mayor(self):
        self.data['clave'] = 100000
        form = CapituloForm(self.data)
        self.assertEqual(
            form.errors['clave'],
            ['Asegúrese de que este valor sea menor o igual a 9000.'])

    def test_capitulo_form_nombre_caracteres_mayor(self):
        self.data['nombre'] = 'SUMINISTROS'*14
        form = CapituloForm(self.data)
        self.assertEqual(
            form.errors['nombre'],
            ['Asegúrese de que este valor tenga menos de 150 caracteres (tiene 154).'])

    def test_capitulo_form_clave_caracteres_numero(self):
        self.data['clave'] = 1000
        form = CapituloForm(self.data)
        self.assertIsInstance(self.data['clave'], int)
