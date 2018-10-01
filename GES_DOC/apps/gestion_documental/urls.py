from django.urls import path
from .views import (
    DocumentoAdmitidoView, 
    DocumentoAdmitidoDeleteView,
    obtener_lista_documentos,
    aprobar_documentos
)

urlpatterns = [
    path('documentacion/', DocumentoAdmitidoView.as_view(), name="SGD_Index"),
    path('documentos/<int:pk>/eliminar/', DocumentoAdmitidoDeleteView.as_view(), name='eliminar_documentos'),
    path('documentos/faltantes/', obtener_lista_documentos, name='documentos_faltantes'),
    path('documentos/aprobar/', aprobar_documentos, name='aprobar_documentos'),
]