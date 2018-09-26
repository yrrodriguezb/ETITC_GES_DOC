from django.contrib import admin
from .models import Documento, DocumentoAdmitido


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fecha_creacion',)
    list_display_links = ('id',)
    readonly_fields = ('fecha_creacion', 'fecha_edicion',)


class DocumentoAdmitidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'archivo', 'aprobado', 'admitido', 'documento', )
    list_display_links = ('id',)
    readonly_fields = ('admitido', 'fecha_creacion', 'fecha_edicion',)


admin.site.register(Documento, DocumentoAdmin)
admin.site.register(DocumentoAdmitido, DocumentoAdmitidoAdmin)


