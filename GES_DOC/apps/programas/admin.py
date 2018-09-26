from django.contrib import admin
from apps.programas.models import Especialidad, Programa


class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fecha_creacion',)
    list_display_links = ('id',)
    readonly_fields = ('fecha_creacion', 'fecha_edicion',)

    def get_actions(self, request):
      actions = super(EspecialidadAdmin, self).get_actions(request)
      if 'delete_selected' in actions:
          del actions['delete_selected']
      return actions

    def has_delete_permission(self, request, obj=None):
        return False


class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion', 'fecha_creacion', 'fecha_edicion',)
    list_display_links = ('id',)
    readonly_fields = ('fecha_creacion', 'fecha_edicion',)

    def get_actions(self, request):
        actions = super(ProgramaAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Programa, ProgramaAdmin)

