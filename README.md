# MasterClass-Django (videoclub)

_Este proyecto es una breve introducción sobre django, entornos virtuales e instalación, a través de un proyecto llamado videoclub. Espero te sea de utilidad._

**¿Qué es Django?**

- Framework web orientado al backend
- World Company de Lawrence, Kansas
- 2005 – Django Reinhardt
- Don't Repeat Yourself
- M-V-T

**Entornos virtuales e Instalación**

- Encapsulaciones o aislamientos de dependencias.

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

### Instalación 🔧

_**Nota:** los comandos se ejecutaron el intérprete de comando de Windows, (en inglés, 'Command Prompt', también conocido como **cmd.exe** o simplemente **cmd**), después de la creación de la carpeta se inicializo el repositorio de git y github, se configuro el archivo gititnore._

1- Crear la carpeta para instalar el entorno virtual:

- Projects> mkdir master-class-django
- Projects> cd master-class-django

2- Instalamos el entorno virtual:

- master-class-django> python -m venv venv

3- Activar el entorno virtual:

- master-class-django> cd venv\Scripts\activate
- Comando para activar el venv: activate
- Comando para desactivar el venv: deactivate

4- Instalar Django en el entorno virtual:

- Scripts> pip install django

5- Verificamos si django está instalado:

- Scripts> python -m django –-version

6- Crea un nuevo proyecto en django:

- Scripts> cd ../../
- master-class-django> django-admin startproject videoclub

7- Crea una nueva aplicación en django:

- master-class-django> cd videoclub
- videoclub> python manage.py startapp movie

8- Inicializar el servidor de desarrollo:

- videoclub> python manage.py runserver

9- Configurar MySQL con Django:

- videoclub> pip install mysqlclient
- **Nota:** Se debe crear la db (moviedb) en el gestor de base de datos de mysql

10- Ejecutar las migraciones para que se aplique en la base de datos:

- videoclub> python manage.py migrate

11- Creación del súper usuario:

- videoclub> python manage.py createsuperuser
- Nombre de usuario (leave blank to use 'xxxxxxx'): admin
- Dirección de correo electrónico: xxxxxxa@hotmail.com
- Password:
- Password (again):
- Superuser created successfully.

12- Inicializar el servidor de desarrollo:

- videoclub> python manage.py runserver

13- Aplicamos la migración de los modelos _(Crea el archivo de migración )_:

- videoclub> python manage.py makemigrations

14- Ejecutar las migraciones para que se aplique en la base de datos:

- videoclub> python manage.py migrate

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Las herramientas utilizadas para este proyecto fueron:_

- [python](https://www.python.org/) - Usado como
  Lenguaje de programación
- [django](https://www.djangoproject.com/) - El framework web usado
- [pip](https://pypi.org/project/Django/) - Sistema de gestión de paquetes

## Autores ✒️

- **Guillermo Garcia Soto** - [Gasogui](https://github.com/Gasogui)

## Expresiones de Gratitud 🎁

- Comenta a otros sobre este proyecto 📢
- Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
- Da las gracias públicamente 🤓.
- etc.

⌨️ con ❤️ por [Gasogui](https://github.com/Gasogui) 😊
