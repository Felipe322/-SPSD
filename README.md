# Sistema Financiero de la Subsecretaría de Prevención del Delito

## Prerrequisitos

- Instalamos VirtualBox. La manera recomendada para implementar este sistema es utilizando [VirtualBox](https://www.virtualbox.org/), para instalarlo puedes seguir las instrucciones para cada sistema operativo haciendo clic [aquí](https://www.virtualbox.org/wiki/Downloads).

- Instalamos Vagrant. La manera recomendada para implementar este sistema es utilizando [Vagrant](https://www.vagrantup.com/), para instalarlo puedes seguir las instrucciones para cada sistema operativo haciendo clic [aquí](https://www.vagrantup.com/downloads).


- Creamos una nueva máquina ubuntu con vagrant:
   ```shell
    $ vagrant init generic/ubuntu1804

   ```

- Una vez instalado vagrant podemos ejecutar el siguiente comando para levantar el entorno(verificar que se encuentre dentro del directorio que contiene el archivo Vagrantfile):

    ```shell
    $ vagrant up
    ```
- Después accedemos a la máquina remota de vagrant:

    ```shell
    $ vagrant ssh
    ```

- Actualiza la lista de paquetes y repositorios:

    ```shell
    $ sudo apt-get update
    ```
- Instalamos el gestor pip3:

    ```shell
    $ sudo apt-get install python3-pip
    ``` 

- Instalamos el servidor de Bases de Datos MariaDB:

    ```shell
    $ sudo apt-get install mariadb-server
    ``` 

- Instalamos las herramientas de desarrollo de python:

    ```shell
    $ sudo apt-get install python-dev
    ``` 

- Instalamos las librerías necesarias para la conexión de python con mariadb:

    ```shell
    $ sudo apt-get install libmysqlclient-dev
    ``` 

- Instalamos a nivel sistema el gestor de entornos virtuales de python:

    ```shell
    $ sudo pip install virtualenv
    ``` 

- Crea el entorno de python llamado "finanzas" y lo activamos:

    ```shell
    $ virtualenv -p python3 env_finanzas

    $ . env_finanzas/bin/activate

    ``` 

- Clonar el repositorio(*Deberá estár autorizado previamente):
   ```shell
   $ git clone https://github.com/adrian052/SPSD

   $ cd SPSD

   ```

## Desarrollo

- Es necesario contar con python 3.9 o superior y pip3 (las pruebas fueron realizadas con la versión 3.9.1). Se recomienda utilizar [pyenv](https://github.com/pyenv/pyenv) como manejador de versiones de python; una vez instalado se pueden seguir los siguientes comandos para instalar la versión deseada de python, esto hay que realizarlo en la raíz del repositorio:

   ```shell
   $ pyenv install 3.9.1
   $ pyenv local 3.9.1
   ```

- Instalamos las dependencias:
   ```shell
    (env_finanzas)$ cd SPSD

    (env_finanzas)$ pip3 install -r requirements.txt
   ```


   Los paquetes que se instalarán son los siguientes:

    Paquete              |  Versión  | 
   ----------------------|-----------|
    django               |   3.1.7   |
    mysqlclient          |   2.0.3   |
    django-mysql         |   3.9     |
    django-environ       |   0.4.5   |
    django-cors-headers  |   3.5.0   |
    Pillow               |   8.1.1   |
    Celery               |   5.0.5   |

### Ejecución del sistema en desarrollo

- Dentro del directorio de SPSD (en donde se encuentra el archivo manage.py) ejecutamos los siguientes comandos:
   ```shell

   (env_finanzas)$ python manage.py makemigrations

   (env_finanzas)$ python manage.py migrate --run-syncdb

   ```

- Crearmos un super usuario para poder acceder al sistema:
   ```shell

   (env_finanzas)$ python manage.py createsuperuser

   ```

- Levantamos el servidor:
   ```shell

   (env_finanzas)$ python manage.py runserver 0:8000

   ```

- Si los comandos fueron exitosos, podremos ingresar a nuestro navegador y verificar que el sistema se ha iniciado con éxito, para esto, ingresamos a la siguiente url: 

    - ip: La ip se determina por la configuración del Vagrantfile (config.vm.network "private_network", ip: "192.168.33.10")

   > http://192.168.33.10:8000
