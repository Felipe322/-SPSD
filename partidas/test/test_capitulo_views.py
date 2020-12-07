from django.test import TestCase
from partidas.models import Capitulo
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.admin_login()

        self.capitulo = Capitulo.objects.create(
            clave=2001,
            nombre='MATERIALES Y SUMINISTROS'
        )

        self.data = {
            'clave': 2001,
            'nombre': 'MATERIALES Y SUMINISTROS'
        }

    def test_crear_capitulo(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        self.assertEqual(respuesta.status_code, 200)

    def test_listado_capitulo(self):
        respuesta = self.client.get('/capitulos/lista/')
        self.assertEqual(respuesta.status_code, 200)

    def test_editar_capitulo(self):
        respuesta = self.client.get(
            '/capitulos/editar/'+str(self.capitulo.clave))
        self.assertEqual(respuesta.status_code, 200)

    def test_template_correcto_nuevo_capitulo(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        self.assertTemplateUsed(respuesta, 'nuevo_capitulo.html')

    def test_template_correcto_lista_capitulo(self):
        respuesta = self.client.get('/capitulos/lista/')
        self.assertTemplateUsed(respuesta, 'lista_capitulos.html')

    def test_template_correcto_editar_capitulo(self):
        respuesta = self.client.get(
            '/capitulos/editar/'+str(self.capitulo.clave))
        self.assertTemplateUsed(respuesta, 'editar_capitulo.html')

    def test_titulo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        titulo = '<title>Nuevo Capitulo</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    def test_titulo_se_encuentra_en_el_template_lista(self):
        respuesta = self.client.get('/capitulos/lista/')
        titulo = '<title>Lista Capitulos</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    def test_titulo_se_encuentra_en_el_template_editar(self):
        respuesta = self.client.get(
            '/capitulos/editar/'+str(self.capitulo.clave))
        titulo = '<title>Actualizar Capitulo</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    # def test_redireccion_al_agregar_capitulo(self):
    #    respuesta = self.client.post('/capitulos/nuevo/', data=self.data)
    #    self.assertEqual(respuesta.url, '/capitulos/lista/')

    # def test_redireccion_al_modificar_capitulo(self):
    #     self.agrega_capitulo()
    #     self.data['nombre'] = 'MATERIALES Y SUMINISTROS2'
    #     respuesta = self.client.post('/capitulos/editar/2000', data=self.data)
    #     self.assertEqual(respuesta.url, '/capitulos/lista/')

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

    def test_titulo_se_encuentra_en_el_template_capitulo(self):
        respuesta = self.client.get('/capitulos/nuevo/')
        formulario = '<h1>Nuevo Capitulo</h1>'
        self.assertInHTML(formulario, str(respuesta.content))

    def test_titulo_lista_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/capitulos/lista/')
        formulario = '<h1>Listado de Capitulos</h1>'
        self.assertInHTML(formulario, str(respuesta.content))

    def test_titulo_actualizar_se_encuentra_en_el_template(self):
        respuesta = self.client.get(
            '/capitulos/editar/'+str(self.capitulo.clave))
        formulario = '<h1>Actualizar Capitulo</h1>'
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
        boton = '<button class="btn btn-success" type="submit">\
            Agregar</button>'
        self.assertInHTML(boton, str(respuesta.content))

    def test_boton_eliminar_capitulo_en_template(self):
        respuesta = self.client.get('/capitulos/lista/')
        boton = '<a class="btn btn-danger" class="btn btn-danger" href="/capitulos/eliminar/'
        boton += str(self.capitulo.clave)+'">Eliminar</a>'
        self.assertInHTML(boton, str(respuesta.content))

    def test_boton_modificar_capitulo_en_template(self):
        respuesta = self.client.get('/capitulos/lista/')
        boton = '<a class="btn btn-primary" href="/capitulos/editar/'
        boton += str(self.capitulo.clave)+'">Modificar</a>'
        self.assertInHTML(boton, str(respuesta.content))

    def agrega_capitulo(self):
        self.capitulo = Capitulo.objects.create(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

    def admin_login(self):
        User.objects.create_user(
            username='admin',
            password='Adri4na203#',
            is_superuser=True
        )
        self.client.login(username='admin', password='Adri4na203#')
