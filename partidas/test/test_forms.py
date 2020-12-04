# from django.test import TestCase
# from partidas.forms import CapituloForm
# from partidas.forms import Capitulo


# class TestFormCapitulo(TestCase):

#     def setUp(self, clave=2001, nombre='MATERIALES Y SUMINISTROS 2'):
#         self.capitulo = Capitulo(
#             clave=clave,
#             nombre=nombre
#         )

#         self.data = {
#             'clave': clave,
#             'nombre': nombre
#         }

#     def test_capitulo_form_valido(self):
#         form = CapituloForm(self.data)
#         self.assertTrue(form.is_valid())

#     # def test_capitulo_form_clave_vacio(self):
#     #     self.data['clave'] = ''
#     #     form = CapituloForm(self.data)
#     #     self.assertEqual(
#     #         form.errors['clave'],
#     #         ['La clave es requerida'])

#     # def test_capitulo_form_nombre_vacio(self):
#     #     self.data['nombre'] = ''
#     #     form = CapituloForm(self.data)
#     #     self.assertEqual(
#     #         form.errors['nombre'],
#     #         ['El nombre es requerido'])

#     def test_capitulo_form_clave_numero_caracteres_correcta(self):
#         self.data['clave'] = 1000
#         form = CapituloForm(self.data)
#         self.assertTrue(form.is_valid())

#     # def test_capitulo_form_clave_numero_caracteres_mayor(self):
#     #     self.data['clave'] = 100000
#     #     form = CapituloForm(self.data)
#     #     self.assertEqual(
#     #         form.errors['clave'],
#     #         ['El número de caracteres de la clave excede el límite'])

#     # def test_capitulo_form_nombre_caracteres_mayor(self):
#     #     self.data['nombre'] = 'SUMINISTROS'*14
#     #     form = CapituloForm(self.data)
#     #     self.assertEqual(
#     #         form.errors['nombre'],
#     #         ['El número de caracteres del nombre excede el límite'])

#     def test_capitulo_form_clave_caracteres_numero(self):
#         self.data['clave'] = 1000
#         form = CapituloForm(self.data)
#         self.assertIsInstance(self.data['clave'], int)

#     # def test_capitulo_form_clave_repetida(self):
#     #     self.data['clave'] = 2200
#     #     form = CapituloForm(self.data)
#     #     self.assertEqual(
#     #         form.errors['clave'],
#     #         ['La clave ya existe.'])
