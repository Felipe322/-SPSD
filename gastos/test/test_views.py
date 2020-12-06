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
        self.define_capitulo()
        self.define_partida()
        self.define_presupuesto()
        self.define_actividad()

        self.gasto = Gasto(
            descripcion=descripcion,
            proveedor=proveedor,
            precio_unitario=precio_unitario,
            cantidad=cantidad,
            precio_total=precio_unitario*cantidad,
            fecha=fecha,
            id_actividad=self.define_actividad()
        )

        self.data = {
            'descripcion': descripcion,
            'proveedor': proveedor,
            'precio_unitario': precio_unitario,
            'cantidad': cantidad,
            'precio_total': precio_unitario*cantidad,
            'fecha': fecha,
            'id_actividad': self.define_actividad()
        }

    def test_crear_gasto(self):
        respuesta = self.client.get('/gastos/nueva/')
        self.assertEqual(respuesta.status_code, 200)

    def test_template_correcto_nuevo_gasto(self):
        respuesta = self.client.get('/gastos/nueva/')
        self.assertTemplateUsed(respuesta, 'nuevo_gasto.html')

    # def test_titulo_se_encuentra_en_el_template(self):
    #     respuesta = self.client.get('/gastos/nueva/')
    #     titulo = '<title>Nuevo Gasto</title>'
    #     self.assertInHTML(titulo, str(respuesta.content))

    # def test_redireccion_al_agregar_gasto(self):
    #     respuesta = self.client.post('/gastos/nueva/',data=self.data)
    #     self.assertEqual(respuesta.url,'/gastos/lista/')

    # def test_redireccion_al_modificar_gasto(self):
    #     self.data['cantidad'] = 320
    #     respuesta = self.client.post('/gastos/editar/1', data=self.data)
    #     self.assertEqual(respuesta.url, '/gastos/lista/')

    # def test_redireccion_al_eliminar_gasto(self):
    #     respuesta = self.client.get('/gastos/eliminar/'+
    # str(Gasto.objects.first().id))#ID??
    #     self.assertEqual(respuesta.url,'/gastos/lista/')

    # def test_lista_gastos(self):
    #    respuesta = self.client.get('/gastos/lista/')
    #    self.assertEqual(respuesta.status_code, 200) #Page not :(

    # def test_lapices_se_encuentre_en_el_template(self):
    #     respuesta = self.client.get('/gastos/lista/')
    #     self.assertContains(respuesta, 'Se compraron muchos lapíces')

    def test_titulo_se_encuentra_en_el_template(self):
        respuesta = self.client.get('/gastos/nueva/')
        formulario = '<h1>Nuevo Gasto</h1>'
        self.assertInHTML(formulario, str(respuesta.content))

    # def test_agregar_gasto_form(self):
    #     capitulo = Capitulo.objects.first()
    #     partida = Partida.objects.first()
    #     presupuesto = Presupuesto.objects.first()
    #     actividad = Actividad.objects.first()
    #     gasto = Gasto.objects.first()
    #     data = {
    #         'descripcion': 'Se compraron muchos lapíces',
    #         'proveedor': 'La comer S.A C.V',
    #         'precio_unitario': 2.50,
    #         'cantidad': 300,
    #         'precio_total': 2.50*300,
    #         'fecha': '2020-12-12',
    #         'id_actividad': Actividad.objects.first()
    #     }
    #     self.client.post('/gastos/editar/'+str(gasto), data=data)
    #     self.assertEqual(
    #         Gasto.objects.first().descripcion,
    # 'Se compraron muchos lapíces')

    # def test_boton_agregar_gasto_en_template(self):
    #     response = self.client.get('/gastos/nueva/')
    #     boton = '<button class="btn btn-success"
    # type="submit">Agregar</button>'
    #     print(response.content)
    #     self.assertInHTML(boton,str(response.content))

    # Definición de campos necesarios para crear un Gasto.
    def define_capitulo(self):
        capitulo = Capitulo(
            clave=2000,
            nombre='MATERIALES Y SUMINISTROS'
        )

    def define_partida(self):
        partida = Partida(
            clave=2110,
            nombre='MATERIALES, ÚTILES Y EQUIPOS MENORES DE OFICINA',
            descripcion='Plumas, borradores, entre otras cosas.',
            capitulo=self.define_capitulo()
        )

    def define_presupuesto(self):
        presupuesto = Presupuesto(
            anio='2020',
            fecha='2020-12-01'
        )

    def define_actividad(self):
        actividad = Actividad(
            programa='27',
            componente='2',
            actividad='3',
            monto=2982.23,
            descripcion='Presupuesto para Febrero',
            mes='02',
            partida=self.define_partida(),
            anio=self.define_presupuesto()
        )

    def admin_login(self):
        user1 = User.objects.create_user(
            username='admin',
            password='Adri4na203#',
            is_superuser=True
        )
        self.client.login(username='admin', password='Adri4na203#')
