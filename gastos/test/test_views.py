from django.test import TestCase
from partidas.forms import Capitulo
from partidas.forms import Partida
from presupuestos.forms import Presupuesto
from presupuestos.forms import Actividad
from gastos.forms import Gasto
from django.contrib.auth.models import User


class TestViewsGasto(TestCase):

    def setUp(self,
              descripcion='Se compraron muchos lapíces',
              proveedor='La comer S.A C.V',
              precio_unitario=2.50,
              cantidad=300,
              fecha='2020-12-12'
              ):

        self.admin_login()

        self.capitulo = Capitulo.objects.create(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

        self.partida = Partida.objects.create(
            clave=2110,
            nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
            descripcion='Plumas, borradores, entre otras cosas.',
            capitulo=self.capitulo
        )

        self.presupuesto = Presupuesto.objects.create(
            anio='2020',
            fecha='2020-12-01'
        )

        self.actividad = Actividad.objects.create(
            programa='27',
            componente='2',
            actividad='3',
            monto=2982.23,
            descripcion='Presupuesto para Febrero',
            mes='02',
            partida=self.partida,
            anio=self.presupuesto
        )

        self.gasto = Gasto.objects.create(
            descripcion=descripcion,
            proveedor=proveedor,
            precio_unitario=precio_unitario,
            cantidad=cantidad,
            precio_total=precio_unitario*cantidad,
            fecha=fecha,
            id_actividad=self.actividad
        )

        self.data = {
            'descripcion': descripcion,
            'proveedor': proveedor,
            'precio_unitario': precio_unitario,
            'cantidad': cantidad,
            'precio_total': precio_unitario*cantidad,
            'fecha': fecha,
            'id_actividad': self.actividad
        }

    def test_crear_gasto(self):
        respuesta = self.client.get('/gastos/nueva/')
        self.assertEqual(respuesta.status_code, 200)

    def test_listado_gasto(self):
        respuesta = self.client.get('/gastos/lista/')
        self.assertEqual(respuesta.status_code, 200)

    def test_editar_gasto(self):
        respuesta = self.client.get('/gastos/editar/'+str(self.gasto.id))
        self.assertEqual(respuesta.status_code, 200)

    def test_template_correcto_nuevo_gasto(self):
        respuesta = self.client.get('/gastos/nueva/')
        self.assertTemplateUsed(respuesta, 'nuevo_gasto.html')

    def test_template_correcto_lista_gasto(self):
        respuesta = self.client.get('/gastos/lista/')
        self.assertTemplateUsed(respuesta, 'lista_gastos.html')

    def test_template_correcto_editar_gasto(self):
        respuesta = self.client.get('/gastos/editar/'+str(self.gasto.id))
        self.assertTemplateUsed(respuesta, 'editar_gasto.html')

    def test_titulo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/gastos/nueva/')
        titulo = '<title>Nuevo Gasto</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    def test_titulo_se_encuentra_en_el_template_lista(self):
        respuesta = self.client.get('/gastos/lista/')
        titulo = '<title>Lista Gastos</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    def test_titulo_se_encuentra_en_el_template_editar(self):
        respuesta = self.client.get('/gastos/editar/'+str(self.gasto.id))
        titulo = '<title>Actualizar Gasto</title>'
        self.assertInHTML(titulo, str(respuesta.content))

    # def test_redireccion_al_agregar_gasto(self):
    #     respuesta = self.client.post('/gastos/nueva/',data=self.data)
    #     self.assertEqual(respuesta.url,'/gastos/lista/')

    # def test_redireccion_al_modificar_gasto(self):
    #     self.data['cantidad'] = 320
    #     respuesta = self.client.post('/gastos/editar/1', data=self.data)
    #     self.assertEqual(respuesta.url, '/gastos/lista/')

    def test_redireccion_al_eliminar_gasto(self):
        respuesta = self.client.get(
            '/gastos/eliminar/'+str(Gasto.objects.first().id))
        self.assertEqual(respuesta.url, '/gastos/lista/')

    def test_lista_gastos(self):
        respuesta = self.client.get('/gastos/lista/')
        self.assertEqual(respuesta.status_code, 200)

    def test_lapices_se_encuentre_en_el_template(self):
        respuesta = self.client.get('/gastos/lista/')
        self.assertContains(respuesta, 'Se compraron muchos lapíces')

    def test_titulo_nuevo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/gastos/nueva/')
        formulario = '<h1>Nuevo Gasto</h1>'
        self.assertInHTML(formulario, str(respuesta.content))

    def test_titulo_lista_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/gastos/lista/')
        formulario = '<h1>Listado de Gastos</h1>'
        self.assertInHTML(formulario, str(respuesta.content))

    def test_titulo_actualizar_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/gastos/editar/'+str(self.gasto.id))
        formulario = '<title>Actualizar Gasto</title>'
        self.assertInHTML(formulario, str(respuesta.content))

    def test_agregar_gasto_form(self):
        gasto = Gasto.objects.first()
        data = {
            'descripcion': 'Se compraron muchos lapíces 2',
            'proveedor': 'La comer S.A C.V',
            'precio_unitario': 2.50,
            'cantidad': 300,
            'precio_total': 2.50*300,
            'fecha': '2020-12-12',
            'id_actividad': Actividad.objects.first().id
        }
        self.client.post('/gastos/editar/'+str(gasto.id), data=data)
        self.assertEqual(
            Gasto.objects.first().descripcion, 'Se compraron muchos lapíces 2')

    def test_boton_agregar_gasto_en_template(self):
        respuesta = self.client.get('/gastos/nueva/')
        boton = '<button class="btn btn-success" type="submit">Agregar</button>'
        self.assertInHTML(boton, str(respuesta.content))

    def test_boton_cancelar_gasto_en_template(self):
        respuesta = self.client.get('/gastos/nueva/')
        boton = '<button class="btn btn-danger" type="reset">Cancelar</button>'
        self.assertInHTML(boton, str(respuesta.content))

    def test_boton_eliminar_gasto_en_lista(self):
        respuesta = self.client.get('/gastos/lista/')
        boton = '<a class="btn btn-danger" href="/gastos/eliminar/'
        boton += str(self.gasto.id)+'">Eliminar</a>'
        self.assertInHTML(boton, str(respuesta.content))

    def test_boton_modificar_gasto_en_lista(self):
        respuesta = self.client.get('/gastos/lista/')
        boton = '<a class="btn btn-primary" href="/gastos/editar/'
        boton += str(self.gasto.id)+'">Modificar</a>'
        self.assertInHTML(boton, str(respuesta.content))

    def admin_login(self):
        user1 = User.objects.create_user(
            username='admin',
            password='Adri4na203#',
            is_superuser=True
        )
        self.client.login(username='admin', password='Adri4na203#')
