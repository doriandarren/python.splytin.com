## Project

## Crear entorno virtual

```sh
## Entorno virtual MacOs
- python3 -m venv .venv
- source .venv/bin/activate                     # Activar entorno
- deactive                                      # Desactivar entorno

## Entorno virtual Windows
- py -m venv .venv                      # Windows
- .\.venv\Scripts\activate                           # Windows
- py -m pip install --upgrade pip      # Windows
- deactivate                                    # Desactivar
- py -m pip xxx                                 # Usar este comando para intrucciones

## Actualizar
pip3 install --upgrade pip


## Instala los requerimientos:
pip3 freeze > requirements.txt                  # Crear archivo requerimientos -> Respaldo / Export
pip3 install -r requirements.txt                # Instalar requerimientos Restore / Import

# Si No se tiene el archivo: requirements.txt
pip install pipreqs                             # Install
pipreqs . --force                               # Ejecutar


## Instalar paquetes
pip3 freeze                                     # Ver Paquetes instalados
py -m pip freeze                                # Para Windows
pip3 install requests                           # Conexion API
pip3 install schedule                           # CronJobs


## Si no funciona VSCode:
( Cmd + Shift + P ) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"
```

## Django

```sh
pip3 install django

django-admin shell                              # Shell de django

## BY PROJECT
django-admin startproject nombre_proyecto       # Crear PROJECT
django-admin startproject nombre_proyecto .     # Crear PROJECT - No crea carpeta duplicada

## BY APP
python3 manage.py startapp nombre_app           # Crear app

python manage.py migrate

python3 manage.py runserver                     # Levantar el servidor
python3 manage.py runserver 8001



```

## -----------------------------
##        Django API
## -----------------------------

## Settings:

```sh

# 1.-
pip3 install django
pip3 install --upgrade pip
django-admin startproject splytin .
python manage.py migrate

# 2.- Instalar django rest
pip3 install djangorestframework          # API  -> Guia https://www.django-rest-framework.org/


# 3.- Añadir splytin/settings.py:
...
INSTALLED_APPS = [
    ...
    'rest_framework',
]
...

# 4.- Instalar Docs -> https://drf-yasg.readthedocs.io/en/stable/readme.html#installation
pip3 install -U drf-yasg

# 5.-  agregar en splytin/settings.py:
...
INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]
...


# 6.- agregar en splytin/urls.py:

...
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]
...

# 7.-  Veirificar si hay migraciones:
python3 manage.py makemigrations


# 8.-  Luego ELIMINAR el sql
-->>> Eliminar el SQLlite

# 9.- Crear app "users":
python3 manage.py startapp users

- También Agregar en "INSTALLED_APPS" y al final del archivo settings.py:
...
INSTALLED_APPS = [
    ...
    'users',
]
...

...
## User
AUTH_USER_MODEL = 'users.User'
...


# 10.- Ir a users -> models.py
## Copiar el archivo
## Luego generar las migraciones:

python3 manage.py makemigrations    ## Crea las migraciones y la DB de nuevo
python3 manage.py migrate           ## Se ejecuta las migraciones


# 11.- Crear el superuser:
python3 manage.py createsuperuser

python3 manage.py makemigrations
python3 manage.py migrate

## Luego modificar users/admin.py
## Copiar el archivo


# 11.- crear carpeta "users/api" con los archivos:

- views.py
- serializers.py
- router.py

## Agregar a las routes principal en splytin/urls.py

...
# USERS
path('api/', include('users.api.router')),
...





## 12.- Instalar JWT -> https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

pip3 install djangorestframework-simplejwt

## Agregar al archivo: settings.py:
...
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
...

## Y en el archivo users/api/router.py:

...
from rest_framework_simplejwt.views import TokenObtainPairView
...
urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    ...
]
...

## También en el mismo archivo agregar (AL FINAL): 

...
import datetime
...
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=120), ## Controla el tiempo de expiración del token
}
...



# 13.- Instalando CORS pagina pypi.org -> https://pypi.org/project/django-cors-headers/

pip3 install django-cors-headers 

## Agregar al archivo: settings.py (buscar linea):
...
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
...

## Y en el mismo fichero (buscar la linea):
...
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",     # ESTA LINEA SOLAMENTE
    "django.middleware.common.CommonMiddleware", # Este ya existe
    ...,
]
...

## Y en el mismo fichero (buscar la linea):
...
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
...


## Y en el mismo fichero (AL FINAL):
...
## CORS
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
...



## RUN SERVER:
python3 manage.py runserver

```



## Ejemplo para CREAR una app::

```sh

## Crear APP Categories:
python3 manage.py startapp categories           # Crear app
python3 -m pip install pillow

## modifica el modelo: categories/models.py
class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories', null=True, blank=True)

    def __str__(self):
        return self.title

## Agregar en settings.py:
...
import os
...
INSTALLED_APPS = [
    ...
    'categories',
]
...
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
...

## Crear migraciones:
python3 manage.py makemigrations
python3 manage.py migrate


## Agregarlo al Panel de administracion (admin):
## Editar categories/admin.py:
...
from django.contrib import admin
from categories.models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
...


## Crear ModelViewSet

## Crear Carpeta API categories/api:

- __init__.py
- views.py
- serializers.py
- router.py

## views.py:
...
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from categories.api.serializers import CategorySerializer
from categories.models import Category

class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
...


## serializers.py:
...
from rest_framework.serializers import ModelSerializer
from categories.models import Category

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image']
...












python3 manage.py runserver

```
