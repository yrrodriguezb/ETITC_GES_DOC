from django.db import models


class Especialidad(models.Model):
    descripcion = models.CharField(max_length=150, unique=True, verbose_name='Descripción')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'
        ordering = ['descripcion', 'fecha_creacion', 'fecha_edicion',]

    def __str__(self):
        return self.descripcion

  
class Programa(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, verbose_name='Especialidad')
    descripcion = models.CharField(max_length=255, unique=True, verbose_name='Descripción')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'
        ordering = ['especialidad', 'descripcion', 'fecha_creacion', 'fecha_edicion',]

    def __str__(self):
        return self.descripcion
