from django.contrib import admin
from .models import Documento, DocumentoAdmitido


class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fecha_creacion',)
    list_display_links = ('id',)
    readonly_fields = ('fecha_creacion', 'fecha_edicion',)


class DocumentoAdmitidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'documento', 'archivo', 'admitido', 'aprobado',)
    list_display_links = ('id',)
    search_fields = ('archivo',)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['admitido', 'documento', 'aprobado', 'fecha_creacion', 'fecha_edicion',]
        else:
            return []


admin.site.register(Documento, DocumentoAdmin)
admin.site.register(DocumentoAdmitido, DocumentoAdmitidoAdmin)


