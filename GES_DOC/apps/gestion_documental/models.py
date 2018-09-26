import os
from time import strftime
from django.db import models
from django.dispatch import receiver
from apps.admitidos.models import Admitido


def custom_upload_to(instance, filename):
    mes, periodo = int(strftime('%m')) , '01'

    if mes > 6 and mes < 13:
        periodo = '02'

    try:
        old_instance = DocumentoAdmitido.objects.get(admitido=instance.admitido, documento=instance.documento)
        old_instance.archivo.delete()
    except:
        pass
    return 'admitidos/{0}/{1}/{2}/{3}'.format(strftime('%Y'), periodo, instance.admitido.pk, filename)


class Documento(models.Model):
    descripcion = models.CharField(max_length=255, verbose_name='Documento')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Documento Requerido'
        verbose_name_plural = 'Documentación Requerida'
        ordering = ['descripcion', 'fecha_creacion', 'fecha_edicion',]

    def __str__(self):
        return self.descripcion


class DocumentoAdmitido(models.Model):
    archivo = models.FileField(upload_to=custom_upload_to, verbose_name='Documento')
    aprobado = models.BooleanField(default=False, verbose_name='Aprobado')
    admitido = models.ForeignKey(Admitido, on_delete=models.PROTECT, verbose_name='Admitido')
    documento = models.ForeignKey(Documento, on_delete=models.PROTECT, verbose_name='Tipo Documento')
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_edicion = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Documento Radicado de Admitidos'
        verbose_name_plural = 'Documentos Radicados de Admitidos'
        ordering = ['admitido', 'fecha_creacion', 'fecha_edicion',]

    def __str__(self):
        return  self.archivo.name


@receiver(models.signals.post_delete, sender=DocumentoAdmitido)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `Media File` object is deleted.
    """
    if instance.archivo:
        if os.path.isfile(instance.archivo.path):
            os.remove(instance.archivo.path)

@receiver(models.signals.pre_save, sender=DocumentoAdmitido)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `Media File` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = DocumentoAdmitido.objects.get(pk=instance.pk).archivo
    except DocumentoAdmitido.DoesNotExist:
        return False

    new_file = instance.archivo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


