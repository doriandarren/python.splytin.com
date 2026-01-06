"""
URL configuration for splytin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
## Docs
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# API USER
from dev.api.router import router_dev
from users.api.router import router_user
from categories.api.router import router_categories
from ai.api.router import router_ollama
from ollama_images.api.router import router_ollama_image
from ollama_texts.api.router import router_ollama_text


schema_view = get_schema_view(
   openapi.Info(
      title="Splkytin - API",
      default_version='v1',
      description="Documentation API Splytin",
      terms_of_service="https://api.splytin.com/policies/terms/",
      contact=openapi.Contact(email="webmaster@splytin.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    #Home
    path('', include('home.urls')),
    
    # Docs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    # API
    
    # Dev
    path('api/v1/', include(router_dev.urls)),
    
    # ADMIN
    path('admin/', admin.site.urls),
    
    # USERS
    path('api/v1/', include('users.api.router')),
    path('api/v1/', include(router_user.urls)),

    # CATEGORIES
    path('api/v1/', include(router_categories.urls)),
    
    # Ollama
    path('api/v1/', include(router_ollama.urls)),
    path('api/v1/', include(router_ollama_image.urls)),
    path('api/v1/', include(router_ollama_text.urls)),
]
