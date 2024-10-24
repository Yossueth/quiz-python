Proyecto Django Hotel
Este documento proporciona una guía paso a paso para configurar y ejecutar el proyecto Django para la gestión de un hotel.

Requisitos Previos
Asegúrate de tener instalado Python y MySQL en tu sistema.

Pasos para Ejecutar el Proyecto
1. Crear la Base de Datos en MySQL
Ejecuta el siguiente comando en tu consola MySQL:

CREATE DATABASE hotel;

2. Instalar MySQL Client para Django
Instala el paquete mysqlclient ejecutando:

pip install mysqlclient

3. Configurar la Conexión a la Base de Datos en Django
Abre el archivo settings.py en la raíz de tu proyecto Django y configura la conexión a la base de datos:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hotel',  # Nombre de la base de datos
        'USER': 'tu_usuario',  # Tu usuario de MySQL
        'PASSWORD': 'tu_contraseña',  # Tu contraseña de MySQL
        'HOST': 'localhost',
        'PORT': '3306',  # Puerto por defecto de MySQL
    }
}

4. Crear una Nueva Aplicación Dentro del Proyecto
Ejecuta el siguiente comando para crear una nueva aplicación llamada api:

python manage.py startapp api

5. Instalar Django REST Framework
Instala Django REST Framework ejecutando:

pip install djangorestframework

6. Agregar Aplicaciones al INSTALLED_APPS
En el archivo settings.py, agrega 'rest_framework', 'tu_proyecto_django', y 'api' a la lista de INSTALLED_APPS:
EJEMPLO:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Django REST Framework
    'api',  # Aplicación API
]
7. Rutas de la API
Las siguientes rutas estarán disponibles una vez que el servidor esté en funcionamiento:

/api/clientes/
/api/habitaciones/
/api/reservas/
/api/pagos/
Para realizar operaciones específicas (DELETE, UPDATE, GET), añade el ID correspondiente después de la ruta.

8. Crear Migraciones
Ejecuta los siguientes comandos para crear y aplicar migraciones:

python manage.py makemigrations

python manage.py migrate

Para deshacer una migración, utiliza:
python manage.py migrate api <codigo_migracion>

9. Ejecutar el Servidor
Inicia el servidor de desarrollo con el siguiente comando:

python manage.py runserver

Ahora tu proyecto Django debería estar en funcionamiento y listo para manejar las operaciones relacionadas con la gestión del hotel. ¡Disfruta programando!
