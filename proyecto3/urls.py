"""
URL configuration for proyecto3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from mascotas.views import crear_mascota, eliminar_mascota, modificar_mascota, listar_mascotas, listar_mascota
from mascotas.views import crear_responsable, modificar_responsable, eliminar_responsable, listar_responsable
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mascota/agregar', crear_mascota),
    path('mascotas', listar_mascotas),
    path('mascota/<int:id>', listar_mascota),
    path('mascota/eliminar/<int:id>', eliminar_mascota),
    path('mascotas/modificar/<int:id>', modificar_mascota),


    path('responsable/agregar', crear_responsable),
    path('responsables', listar_responsable),
    path('responsable/modificar/<id>', modificar_responsable),
    path('responsable/eliminar/<id>', eliminar_responsable),

]