# from django.test import TestCase
# from partidas.forms import CapituloForm
# from partidas.forms import Capitulo
# from django.core.exceptions import ValidationError

# class TestModelsCapitulo(TestCase):

#     def setUp(self, clave = 2001, nombre = 'MATERIALES Y SUMINISTROS 2'):
#         self.capitulo = Capitulo(
#             clave=clave,
#             nombre=nombre
#         )

#         self.data = {
#             'clave': clave,
#             'nombre': nombre
#         }

#     def test_capitulo_duplicado(self):
#         self.capitulo.save()
#         capitulo_repetido = Capitulo(
#             clave= 2001,
#             nombre='MATERIALES Y SUMINISTROS'
#         )
#         try:
#             capitulo_repetido.full_clean()
#         except ValidationError as ex:
#             msg = str(ex.message_dict['clave'][0])
#             self.assertEqual(
#                 msg,
#                 'Ya existe un/a Capitulo con este/a Clave.')

#     def test_capitulo_clave_minimo_caracteres(self):
#         self.capitulo.save()
#         self.capitulo.clave = 18
#         with self.assertRaises(ValidationError):
#             self.capitulo.full_clean()
