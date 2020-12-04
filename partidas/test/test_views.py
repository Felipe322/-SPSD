# from django.test import TestCase
# from django.urls import reverse
# from partidas.models import Capitulo
# from django.contrib.auth.models import User, Permission
# from django.contrib.auth.models import Group
# from django.template.response import SimpleTemplateResponse

# class TestViews(TestCase):
#     def setUp(self):
#         self.capitulo = Capitulo(
#             clave=4001,
#             nombre='MATERIALES Y SUMINISTROS'
#         )

#         self.data = {
#             'clave': 4001,
#             'nombre': 'MATERIALES Y SUMINISTROS'
#         }

#     def test_crear_capitulo(self):
#         #Hace login como admin antes
#         respuesta = self.client.get('/capitulos/nuevo/')
#         self.assertEqual(respuesta.status_code, 200)

#     def test_template_correcto_nuevo_capitulo(self):
#         #Hace login como admin antes
#         respuesta = self.client.get('/capitulos/nuevo/')
#         self.assertTemplateUsed(respuesta, 'nuevo_capitulo.html')

#     # def test_titulo_se_encuentra_en_el_template(self):
#     #     respuesta = self.client.get('/capitulos/nuevo/')
#     #     titulo = '<title>Nuevo Capitulo</title>'
#     #     self.assertInHTML(titulo, respuesta.rendered_content)


#     # def test_redireccion_(self):
#     #     respuesta = SimpleTemplateResponse(self.client.get('/capitulos/nuevo/'))
#     #     self.assertEqual(respuesta.url,'/capitulos/lista/')