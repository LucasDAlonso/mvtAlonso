from django.urls import path
from .views import inicio, ver_fecha, saludo, mi_template, listado_familiares

urlpatterns = [
    path('', inicio),
    path('fecha/', ver_fecha),
    path('saludo/<nombre>/', saludo),
    path('mi-template/<nombre_fam>/<edad_fam>/<fecha_fam>/', mi_template),
    path('listado-familiares/', listado_familiares),
  
]