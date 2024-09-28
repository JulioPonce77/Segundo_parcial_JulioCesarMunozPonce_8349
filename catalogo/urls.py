from django.urls import path

from .views import (
    listar_profesores,
    crear_profesor,
    modificar_profesor,
    eliminar_profesor,
    listar_mascotas,
    crear_mascota,
    modificar_mascota,
    eliminar_mascota
)

urlpatterns = [
    path('', home_view, name='home'),
    path('profesores/', listar_profesores, name='listar_profesores'),
    path('profesores/crear/', crear_profesor, name='crear_profesor'),
    path('profesores/modificar/<int:pk>/', modificar_profesor, name='modificar_profesor'),
    path('profesores/eliminar/<int:pk>/', eliminar_profesor, name='eliminar_profesor'),
    path('mascotas/', listar_mascotas, name='listar_mascotas'),
    path('mascotas/crear/', crear_mascota, name='crear_mascota'),
    path('mascotas/modificar/<int:pk>/', modificar_mascota, name='modificar_mascota'),
    path('mascotas/eliminar/<int:pk>/', eliminar_mascota, name='eliminar_mascota'),
    
]
