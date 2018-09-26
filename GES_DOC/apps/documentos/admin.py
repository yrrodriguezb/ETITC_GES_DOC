from django.contrib import admin
from apps.documentos.models import TipoDocumento


class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'fecha_creacion',)
    list_display_links = ('codigo',)
    readonly_fields = ('fecha_creacion', 'fecha_edicion',)

    def get_actions(self, request):
      actions = super(TipoDocumentoAdmin, self).get_actions(request)
      if 'delete_selected' in actions:
          del actions['delete_selected']
      return actions

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(TipoDocumento, TipoDocumentoAdmin)


