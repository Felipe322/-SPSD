from django.test import TestCase
from django.urls import reverse
from presupuestos.models import (Actividad, Presupuesto)
from partidas.models import (Partida,Capitulo)
from django.contrib.auth.models import User, Permission
from django.contrib.auth.models import Group
from django.template.response import SimpleTemplateResponse
import datetime




class TestViews(TestCase):
	def setUp(self):
		self.actividad = Actividad(
			programa='27', 
			componente='2', 
			actividad='3',
			monto=2982.23,
			descripcion='Presupuesto para Febrero',
			mes = '02',
			partida = self.define_partida(),
			anio = self.define_presupuesto()
		)

		self.data = {
			'programa':'27', 
			'componente':'2', 
			'actividad':'3',
			'monto':2982.23,
			'descripcion':'Presupuesto para Febrero',
			'mes':'02',
			'partida':self.define_partida(),
			'anio':self.define_presupuesto()
		}


	def define_capitulo(self):
		capitulo = Capitulo.objects.create(
			clave=2000,
			nombre='MATERIALES Y SUMINISTROS'
		)


	def define_partida(self):
		partida = Partida.objects.create(
			clave=2110,
			nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
			descripcion='Plumas, borradores, entre otras cosas.',
			capitulo=self.define_capitulo()
		)

	def define_presupuesto(self):
		presupuesto = Presupuesto.objects.create(
			anio='2020',
			fecha='2020-12-3'
		)


	def test_crear_presupuesto(self):
		self.admin_login()
		respuesta = self.client.get('/actividades/nueva/')
		self.assertEqual(respuesta.status_code,200)

	
	def test_template_correcto_nueva_actividad(self):
		self.admin_login()
		respuesta = self.client.get('/actividades/nueva/')
		self.assertTemplateUsed(respuesta, 'nueva_actividad.html')

	
	def test_titulo_actividades_se_encuentra_en_el_template(self):
		self.admin_login()
		respuesta = self.client.get('/actividades/nueva/')
		titulo = '<title>Nueva Actividad</title>'
		self.assertIn(titulo, str(respuesta.content))

	'''
	def test_redireccion_al_agregar_actividad(self): #le falta
		self.admin_login()
		respuesta = self.client.post('/actividades/nueva/',data=self.data)
		self.assertEqual(respuesta.url,'/actividades/lista/')
	'''

	'''
	def test_redireccion_al_modificar_actividad(self): #le falta
		self.admin_login()
		self.agrega_actividad()
		self.data['monto'] = 20,000.00
		respuesta = self.client.post('/actividades/editar/1',data=self.data)
		self.assertEqual(respuesta.url,'/actividades/lista/')

	'''
	'''
	def test_redireccion_al_eliminar_actividad(self): #le falta
		self.admin_login()
		self.agrega_actividad()
		respuesta = self.client.get('/actividades/eliminar/1')
		self.assertEqual(respuesta.url,'/actividades/lista/')
	'''

	'''
	def test_lista_actividades(self):
		self.admin_login()
		respuesta = self.client.get('/actividades/lista/')
		self.assertEqual(respuesta.status_code, 200)
	'''

	'''
	def test_programa_1_se_encuentre_en_el_template(self): #le falta
		self.admin_login()
		self.agrega_actividad()
		respuesta = self.client.get('/actividades/lista/')
		self.assertContains(respuesta, 1)
	'''

	'''
	def test_titulo_actividades_lista_se_encuentra_en_el_template(self):
		self.admin_login()
		respuesta = self.client.get('/actividades/lista/')
		titulo = '<h1>Listado de Actividades</h1>'
		self.assertInHTML(titulo, str(respuesta.content))
	'''


	'''
	def test_boton_agregar_actividad_en_template(self):
		self.admin_login()
		response = self.client.get('/actividades/nueva/')
		boton = '<button class="btn btn-success" , type="submit">Agregar</button>'
		self.assertInHTML(boton,str(response.content))
	'''


	'''
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
	'''



	def agrega_actividad(self):
		self.actividad = Actividad.objects.create(
			programa='27', 
			componente='2', 
			actividad='3',
			monto=2982.23,
			descripcion='Presupuesto para Febrero',
			mes = '02',
			partida = self.define_partida(),
			anio = self.define_presupuesto()
		)


	def admin_login(self):
		user1 = User.objects.create_user(
			username='admin',
			password='Adri4na203#',
			is_superuser=True
		)
		self.client.login(username='admin', password='Adri4na203#')