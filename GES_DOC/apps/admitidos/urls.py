from django.urls import path
from .views import obtener_programas, obtener_tipo_documentos, obtener_sesion_admitido


urlpatterns = [
    path('programas/', obtener_programas, name="programas"),
    path('tipo_documentos/', obtener_tipo_documentos, name="tipo_documentos"),
    path('sesion/', obtener_sesion_admitido, name='sesion_admitido'),
]