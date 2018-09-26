from django.contrib import admin
from apps.admitidos.models import Admitido


class AdmitidoAdmin(admin.ModelAdmin):

    def formato_fecha_creacion(self, obj):
        return obj.fecha_creacion.strftime("%d/%m/%Y %H:%M:%S")
    
    def formato_fecha_edicion(self, obj):
        return obj.fecha_edicion.strftime("%d/%m/%Y %H:%M:%S")
    
    formato_fecha_creacion.short_description = "Fecha Creación"
    formato_fecha_edicion.short_description = "Última Modificación"

    list_display = (
        'id', 
        'tipo_documento',
        'numero_identificacion',
        'primer_nombre',
        'segundo_nombre',
        'primer_apellido',
        'segundo_apellido',
        'programa',
        'periodo_academico',
        'formato_fecha_creacion',
        'formato_fecha_edicion',
    )
    list_display_links = ('id',)
    readonly_fields = ('fecha_creacion', 'fecha_edicion',)


admin.site.register(Admitido, AdmitidoAdmin)
