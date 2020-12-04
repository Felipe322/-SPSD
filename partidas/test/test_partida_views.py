# from django.test import TestCase
# from django.urls import reverse
# from partidas.models import Partida
# from partidas.models import Capitulo


# class TestViews(TestCase):

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

    # def test_crear_partida(self):
    #     #Hace login como admin antes
    #     respuesta = self.client.get('/partidas/nueva/')
    #     self.assertEqual(respuesta.status_code, 200)

    # def test_template_correcto_nueva_partida(self):
    #     #Hace login como admin antes
    #     respuesta = self.client.get('/partidas/nueva/')
    #     self.assertTemplateUsed(respuesta, 'nueva_partida.html')

    # def test_titulo_se_encuentra_en_el_template(self): #Err
    #     respuesta = self.client.get('/partidas/nueva/')
    #     titulo = '<title>Nueva Partida</title>'
    #     self.assertInHTML(titulo, respuesta.rendered_content)