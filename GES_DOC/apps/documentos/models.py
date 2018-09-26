from django.db import models


class TipoDocumento(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True, verbose_name='Código')
    descripcion = models.CharField(max_length=150, verbose_name='Descripción')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Tipo Documento de Identidad'
        verbose_name_plural = 'Tipos Documento de Identidad'
        ordering = ['codigo', 'descripcion', 'fecha_creacion', 'fecha_edicion',]

    def __str__(self):
        return self.descripcion