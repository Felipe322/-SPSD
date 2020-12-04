# from django.test import TestCase
# from partidas.forms import PartidaForm
# from partidas.forms import Partida
# from partidas.forms import Capitulo

# class TestFormPartida(TestCase):

#     def setUp(self, clave=2110, nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA', descripcion='Plumas, borradores, entre otras cosas.'):
#         capitulo=Capitulo(
#             clave=2000,
#             nombre='MATERIALES Y SUMINISTROS'
#         )

#         self.partida = Partida(
#             clave=clave,
#             nombre=nombre,
#             descripcion=descripcion,
#             capitulo=capitulo
#         )

#         self.data = {
#             'clave': clave,
#             'nombre': nombre,
#             'descripcion': descripcion,
#             'capitulo': capitulo
#         }

#     def test_partida_form_valido(self):#Err
#         form = PartidaForm(self.data)
#         self.assertTrue(form.is_valid())

#     def test_partida_form_clave_vacio(self):
#         self.data['clave'] = ''
#         form = PartidaForm(self.data)
#         self.assertEqual(
#             form.errors['clave'],
#             ['La clave es requerida.']) Cambiar msg en interfaz

#     def test_partida_form_nombre_vacio(self):
#         self.data['nombre'] = ''
#         form = PartidaForm(self.data)
#         self.assertEqual(
#             form.errors['nombre'],
#             ['El nombre es requerido.']) Cambiar msg en interfaz

#     def test_partida_form_descripcion_vacio(self):
#         self.data['descripcion'] = ''
#         form = PartidaForm(self.data)
#         self.assertEqual(
#             form.errors['descripcion'],
#             ['La descripción es requerida.']) Cambiar msg en interfaz

#     def test_partida_form_capitulo_vacio(self):
#         self.data['capitulo'] = ''
#         form = PartidaForm(self.data)
#         self.assertEqual(
#             form.errors['capitulo'],
#             ['El capítulo es requerido.']) Cambiar msg en interfaz

#     def test_partida_form_clave_numero_caracteres_correcta(self):#Err
#         self.data['clave'] = 2115
#         form = PartidaForm(self.data)
#         self.assertTrue(form.is_valid())

#     def test_partida_form_clave_numero_caracteres_mayor(self):
#         self.data['clave'] = 200003
#         form = PartidaForm(self.data)
#         self.assertEqual(
#             form.errors['clave'],
#             ['El número de caracteres de la clave excede el límite.']) Cambiar msg en interfaz

#     def test_partida_form_nombre_caracteres_mayor(self):
#         self.data['nombre'] = 'MATERIALES Y ÚTILES'*5
#         form = PartidaForm(self.data)
#         self.assertEqual(
#             form.errors['nombre'],
#             ['El número de caracteres del nombre excede el límite.']) Cambiar msg en interfaz

#     def test_partida_form_descripcion_caracteres_mayor(self): #Err
#         self.data['descripcion'] = 'Plumas, borradores y más.'*10 #Cambiar a más alto en la bd unos 3000
#         form = PartidaForm(self.data)
#         self.assertEqual(
#             form.errors['descripcion'],
#             ['El número de caracteres de la descripción excede el límite.']) #Cambiar msg en interfaz

#     def test_partida_form_clave_caracteres_numero(self):
#         self.data['clave'] = 2200
#         form = PartidaForm(self.data)
#         self.assertIsInstance(self.data['clave'], int)

#     def test_partida_form_clave_repetida(self): #Err
#         self.data['clave'] = 2110
#         form = PartidaForm(self.data)
#         self.assertEqual(
#             form.errors['clave'],
#             ['La clave ya existe.'])