from django.test import TestCase
from django.urls import reverse
from partidas.models import Capitulo
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.admin_login()

        self.capitulo = Capitulo(
            clave=4001,
            nombre='MATERIALES Y SUMINISTROS'
        )

        self.data = {
            'clave': 4001,
            'nombre': 'MATERIALES Y SUMINISTROS'
        }

    def test_crear_capitulo(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        self.assertEqual(respuesta.status_code, 200)

    def test_template_correcto_nuevo_capitulo(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        self.assertTemplateUsed(respuesta, 'nuevo_capitulo.html')

    def test_titulo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        titulo = '<title>Nuevo Capitulo</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    def test_redireccion_al_agregar_capitulo(self):
        respuesta = self.client.post('/capitulos/nuevo/', data=self.data)
        self.assertEqual(respuesta.url, '/capitulos/lista/')

    def test_redireccion_al_modificar_capitulo(self):
        self.agrega_capitulo()
        self.data['nombre'] = 'MATERIALES Y SUMINISTROS2'
        respuesta = self.client.post('/capitulos/editar/2000', data=self.data)
        self.assertEqual(respuesta.url, '/capitulos/lista/')

    def test_redireccion_al_eliminar_capitulo(self):
        self.agrega_capitulo()
        respuesta = self.client.get('/capitulos/eliminar/2000')
        self.assertEqual(respuesta.url, '/capitulos/lista/')

    def test_lista_capitulo(self):
        respuesta = self.client.get('/capitulos/lista/')
        self.assertEqual(respuesta.status_code, 200)

    def test_materiales_se_encuentre_en_el_template(self):
        self.agrega_capitulo()
        respuesta = self.client.get('/capitulos/lista/')
        self.assertContains(respuesta, 'MATERIALES Y SUMINISTROS')

    def test_titulo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        formulario = '<h1>Nuevo Capitulo</h1>'
        self.assertInHTML(formulario, str(respuesta.content))

    def test_agregar_capitulo_form(self):
        self.agrega_capitulo()
        id = Capitulo.objects.first().clave
        data = {
            'clave': '2000',
            'nombre': 'MATERIALES Y SUMINISTROS',
        }
        self.client.post('/capitulos/editar/'+str(id), data=data)
        self.assertEqual(
            Capitulo.objects.first().nombre, 'MATERIALES Y SUMINISTROS')

    def test_boton_agregar_capitulo_en_template(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        boton = '<button class="btn btn-success" type="submit">Agregar</button>'
        self.assertInHTML(boton, str(respuesta.content))

    def agrega_capitulo(self):
        self.capitulo = Capitulo.objects.create(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

    def admin_login(self):
        user1 = User.objects.create_user(
            username='admin',
            password='Adri4na203#',
            is_superuser=True
        )
        self.client.login(username='admin', password='Adri4na203#')
