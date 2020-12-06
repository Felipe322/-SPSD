from django.test import TestCase
from partidas.forms import Capitulo
from partidas.forms import Partida
from presupuestos.forms import Presupuesto
from presupuestos.forms import Actividad
from gastos.forms import GastoForm
from gastos.forms import Gasto


class TestFormsGasto(TestCase):

    def setUp(self, descripcion='Se compraron muchos lapízes',
              proveedor='La comer S.A C.V',
              precio_unitario=2.50,
              cantidad=300,
              fecha='2020-12-12'
              ):

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

    # def test_gasto_form_valido(self):
    #     form = GastoForm(self.data)
    #     print(form.errors)
    #     self.assertTrue(form.is_valid())

    def test_gasto_form_descripcion_vacia(self):
        self.data['descripcion'] = ''
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['descripcion'],
            ['Este campo es obligatorio.'])

    def test_gasto_form_proveedor_vacio(self):
        self.data['proveedor'] = ''
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['proveedor'],
            ['Este campo es obligatorio.'])

    def test_gasto_form_precio_unitario_vacio(self):
        self.data['precio_unitario'] = ''
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['precio_unitario'],
            ['Este campo es obligatorio.'])

    def test_gasto_form_cantidad_vacio(self):
        self.data['cantidad'] = ''
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['cantidad'],
            ['Este campo es obligatorio.'])

    def test_gasto_form_fecha_vacio(self):
        self.data['fecha'] = ''
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['fecha'],
            ['Este campo es obligatorio.'])

    def test_gasto_form_id_actividad_vacio(self):
        self.data['id_actividad'] = ''
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['id_actividad'],
            ['Este campo es obligatorio.'])

    def test_gasto_form_descripcion_caracteres_mayor(self):
        self.data['descripcion'] = 'descripción' * \
            300  # Aumentar a 3 mil en la BD
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['descripcion'],
            ['Asegúrese de que este valor tenga menos de 256 caracteres (tiene 3300).'])

    def test_gasto_form_proveedor_caracteres_mayor(self):
        self.data['proveedor'] = 'La comer S.A C.V'*13
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['proveedor'],
            ['Asegúrese de que este valor tenga menos de 200 caracteres (tiene 208).'])

    # def test_gasto_form_precio_unitario_numeros_mayor(self):#Err válidar en iterfaz
    #     self.data['precio_unitario'] = 1000000001 #Cambiar Válor (es mucho)
    #     form = GastoForm(self.data)
    #     self.assertEqual(
    #         form.errors['precio_unitario'],
    #         ['El precio unitario excede el límite.'])

    def test_gasto_form_cantidad_numeros_mayor(self):
        self.data['cantidad'] = 100001  # Aumentar
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['cantidad'],
            ['Asegúrese de que este valor sea menor o igual a 100000.'])

    # def test_gasto_form_precio_unitario_numeros_mayor_cero(self): #ERROR ELIMINAR A LA BREVEDAD.
    #     self.data['precio_unitario'] = -1 #VALIDAR QUE SEA POSITIVO!!
    #     form = GastoForm(self.data)
    #     self.assertEqual(
    #         form.errors['precio_unitario'],
    #         ['El precio unitario debe de ser mayor a cero.'])

    # def test_gasto_form_precio_unitario_numeros_validos(self): #ERROR ELIMINAR A LA BREVEDAD.
    #     self.data['precio_unitario'] = 2.50
    #     form = GastoForm(self.data)
    #     self.assertTrue(form.is_valid())

    def test_gasto_form_cantidad_numeros_mayor_cero(self):
        self.data['cantidad'] = -100  # VALIDAR QUE SEA POSITIVO!!
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['cantidad'],
            ['Asegúrese de que este valor sea mayor o igual a 0.'])

    # def test_gasto_form_cantidad_numeros_validos(self): #Err
    #     self.data['cantidad'] = 301
    #     form = GastoForm(self.data)
    #     self.assertTrue(form.is_valid())

    def test_gasto_form_fecha_no_valida(self):
        self.data['fecha'] = '1010-88-1'
        form = GastoForm(self.data)
        self.assertEqual(
            form.errors['fecha'],
            ['Introduzca una fecha válida.'])

    # def test_gasto_form_fecha_valida(self): #ERR
    #     self.data['fecha'] = '2020-03-12'
    #     form = GastoForm(self.data)
    #     self.assertTrue(form.is_valid())

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
