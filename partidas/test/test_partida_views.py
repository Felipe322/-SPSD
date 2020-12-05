from django.test import TestCase
from django.urls import reverse
from partidas.models import Partida
from partidas.models import Capitulo
from django.contrib.auth.models import User, Permission
from django.contrib.auth.models import Group
from django.template.response import SimpleTemplateResponse

class TestViews(TestCase):

    def setUp(self, clave=2110, nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA', descripcion='Plumas, borradores, entre otras cosas.'):
        self.admin_login()
        capitulo=Capitulo.objects.create(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

        self.partida = Partida(
            clave=clave,
            nombre=nombre,
            descripcion=descripcion,
            capitulo=capitulo
        )

        self.data = {
            'clave': clave,
            'nombre': nombre,
            'descripcion': descripcion,
            'capitulo': capitulo
        }

    def test_crear_partida(self):
        respuesta = self.client.get('/partidas/nueva/')
        self.assertEqual(respuesta.status_code, 200)

    def test_template_correcto_nueva_partida(self):
        respuesta = self.client.get('/partidas/nueva/')
        self.assertTemplateUsed(respuesta, 'nueva_partida.html')

    def test_titulo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/partidas/nueva/')
        titulo = '<title>Nueva Partida</title>'
        self.assertInHTML(titulo, str(respuesta.content))



############################


#     def test_redireccion_al_agregar_capitulo(self):
#         respuesta = self.client.post('/capitulos/nuevo/',data=self.data)
#         self.assertEqual(respuesta.url,'/capitulos/lista/')

#     def test_redireccion_al_modificar_capitulo(self):
#         self.agrega_capitulo()
#         self.data['nombre'] = 'MATERIALES Y SUMINISTROS2'
#         respuesta = self.client.post('/capitulos/editar/2000',data=self.data)
#         self.assertEqual(respuesta.url,'/capitulos/lista/')

#     def test_redireccion_al_eliminar_capitulo(self):
#         self.agrega_capitulo()
#         respuesta = self.client.get('/capitulos/eliminar/2000')
#         self.assertEqual(respuesta.url,'/capitulos/lista/')

#     def test_lista_capitulo(self):
#        respuesta = self.client.get('/capitulos/lista/')
#        self.assertEqual(respuesta.status_code, 200)

#     def test_materiales_se_encuentre_en_el_template(self):
#         self.agrega_capitulo()
#         respuesta = self.client.get('/capitulos/lista/')
#         self.assertContains(respuesta, 'MATERIALES Y SUMINISTROS')

#     def test_titulo_se_encuentra_en_el_template(self):
#         response = self.client.get('/capitulos/nuevo/')
#         formulario = '<h1>Nuevo Capitulo</h1>'
#         self.assertInHTML(formulario, str(response.content))

#     def test_agregar_capitulo_form(self):
#         self.agrega_capitulo()
#         id = Capitulo.objects.first().clave
#         data = {
#             'clave': '2000',
#             'nombre': 'MATERIALES Y SUMINISTROS',
#         }
#         self.client.post('/capitulos/editar/'+str(id), data=data)
#         self.assertEqual(
#             Capitulo.objects.first().nombre, 'MATERIALES Y SUMINISTROS')

#     def test_boton_agregar_capitulo_en_template(self):
#         response = self.client.get('/capitulos/nuevo/')
#         boton = '<button class="btn btn-success" type="submit">Agregar</button>'
#         self.assertInHTML(boton,str(response.content))
#     def agrega_capitulo(self):
#        self.capitulo = Capitulo.objects.create(
#            clave=2000,
#            nombre='MATERIALES Y SUMINISTROS'
#        )
    def admin_login(self):
        user1 = User.objects.create_user(
            username='admin',
            password='Adri4na203#',
            is_superuser=True
        )
        self.client.login(username='admin', password='Adri4na203#')