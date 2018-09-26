import time

from django.db import models
from apps.documentos.models import TipoDocumento
from apps.programas.models import Programa


class Admitido(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.PROTECT, verbose_name='Tipo de Documento')
    numero_identificacion = models.CharField(max_length=20, verbose_name='Número de Identificación')
    primer_nombre = models.CharField(max_length=50, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=50, verbose_name='Segundo Nombre', null=True, blank=True)
    primer_apellido = models.CharField(max_length=50, verbose_name='Primer Apellido')
    segundo_apellido = models.CharField(max_length=50, verbose_name='Segundo Apellido', null=True, blank=True)
    programa = models.ForeignKey(Programa, on_delete=models.PROTECT, verbose_name='Programa')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def anio_actual():
        return '{}'.format(time.strftime('%Y'))

    def periodo_actual():
        periodo = '01'
        mes_actual = int(time.strftime('%m'))
        if mes_actual > 6 and mes_actual < 13:
            periodo = '02'
        return '{}'.format(periodo)

    anio = models.CharField(max_length=4, default=anio_actual, editable=False, verbose_name='Año')
    periodo = models.CharField(max_length=2, default=periodo_actual, editable=False, verbose_name='Período')
    
    @property
    def periodo_academico(self):
        return '{}{}'.format(self.anio, self.periodo)

    class Meta:
        verbose_name = 'Admitido'
        verbose_name_plural = 'Admitidos'
        ordering = [
          'programa', 
          'tipo_documento', 
          'primer_apellido', 
          'segundo_apellido',
          'primer_nombre',
          'segundo_nombre',
        ]

    def __str__(self):
        return '{} {} {} {}'.format(
          self.primer_nombre,
          self.segundo_nombre or '',
          self.primer_apellido,
          self.segundo_apellido or ''
        )