from django.contrib import admin
from apps.admitidos.models import Admitido
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from import_export.formats import base_formats


class AdmitidoResource(resources.ModelResource):

    class Meta:
        model = Admitido

        import_id_fields = [
            'tipo_documento',
            'numero_identificacion',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'programa',
            'jornada',
        ]

        exclude = ('fecha_creacion','fecha_edicion', )

        fields = (
            'tipo_documento',
            'numero_identificacion',
            'primer_nombre',
            'segundo_nombre',
            'primer_apellido',
            'segundo_apellido',
            'programa',
            'jornada',
        )

    
@admin.register(Admitido)
class AdmitidoResourceAdmin(ImportExportModelAdmin):
    
    def formato_fecha_creacion(self, obj):
        return obj.fecha_creacion.strftime("%d/%m/%Y %H:%M:%S")
    
    def formato_fecha_edicion(self, obj):
        return obj.fecha_edicion.strftime("%d/%m/%Y %H:%M:%S")

    def get_export_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
        )
        return [f for f in formats if f().can_export()]
    
    def get_import_formats(self):
        formats = (
            base_formats.CSV,
            base_formats.XLS,
        )
        return [f for f in formats if f().can_import()]
    
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
    
    resource_class = AdmitidoResource
    
    search_fields = ('numero_identificacion',)
    
    list_filter = (
        ('programa', RelatedDropdownFilter),
    )