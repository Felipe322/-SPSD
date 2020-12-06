from django.test import TestCase
from django.urls import reverse
from presupuestos.models import Presupuesto
from django.contrib.auth.models import User
import datetime


class TestViews(TestCase):
    def setUp(self):
        self.presupuesto = Presupuesto(
            anio='2020',
            fecha='2020-09-11'
        )

        self.data = {
            'anio': '2020',
            'fecha': '2020-09-11'
        }

    def test_crear_presupuesto(self):
        self.admin_login()
        respuesta = self.client.get('/presupuestos/nuevo/')
        self.assertEqual(respuesta.status_code, 200)

    def test_template_correcto_nuevo_capitulo(self):
        self.admin_login()
        respuesta = self.client.get('/presupuestos/nuevo/')
        self.assertTemplateUsed(respuesta, 'nuevo_presupuesto.html')

    def test_titulo_prespuestos_se_encuentra_en_el_template(self):
        self.admin_login()
        respuesta = self.client.get('/presupuestos/nuevo/')
        titulo = '<title>Nuevo Presupuesto</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    def test_redireccion_al_agregar_presupuesto(self):
        self.admin_login()
        respuesta = self.client.post('/presupuestos/nuevo/', data=self.data)
        self.assertEqual(respuesta.url, '/presupuestos/lista/')

    def test_redireccion_al_modificar_presupuesto(self):
        self.admin_login()
        self.agrega_presupuesto()
        self.data['fecha'] = '2020-01-01'
        respuesta = self.client.post(
            '/presupuestos/editar/2020', data=self.data)
        self.assertEqual(respuesta.url, '/presupuestos/lista/')

    def test_redireccion_al_eliminar_presupuesto(self):
        self.admin_login()
        self.agrega_presupuesto()
        respuesta = self.client.get('/presupuestos/eliminar/2020')
        self.assertEqual(respuesta.url, '/presupuestos/lista/')

    def test_lista_presupuesto(self):
        self.admin_login()
        respuesta = self.client.get('/presupuestos/lista/')
        self.assertEqual(respuesta.status_code, 200)

    def test_año_2020_se_encuentre_en_el_template(self):
        self.admin_login()
        self.agrega_presupuesto()
        respuesta = self.client.get('/presupuestos/lista/')
        self.assertContains(respuesta, '2020')

    def test_titulo_presupuesto_lista_se_encuentra_en_el_template(self):
        self.admin_login()
        respuesta = self.client.get('/presupuestos/lista/')
        titulo = '<h1>Listado de Presupuestos</h1>'
        self.assertInHTML(titulo, str(respuesta.content))

    def test_agregar_presupuesto_form(self):
        self.admin_login()
        self.agrega_presupuesto()
        id = Presupuesto.objects.first().anio
        data = {
            'anio': '2020',
            'fecha': '2020-01-02',
        }
        self.client.post('/presupuestos/editar/'+str(id), data=data)
        self.assertEqual(
            Presupuesto.objects.first().fecha, datetime.date(2020, 1, 2))

    def test_boton_agregar_presupuesto_en_template(self):
        self.admin_login()
        response = self.client.get('/presupuestos/nuevo/')
        boton = '<button class="btn btn-success" ,\
            type="submit">Agregar</button>'
        self.assertInHTML(boton, str(response.content))

    def agrega_presupuesto(self):
        self.presupuesto = Presupuesto.objects.create(
            anio='2020',
            fecha='2020-02-02'
        )

    def admin_login(self):
        user1 = User.objects.create_user(
            username='admin',
            password='Adri4na203#',
            is_superuser=True
        )
        self.client.login(username='admin', password='Adri4na203#')
