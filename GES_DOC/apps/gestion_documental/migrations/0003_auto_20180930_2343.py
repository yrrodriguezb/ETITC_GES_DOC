# Generated by Django 2.0.2 on 2018-09-30 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_documental', '0002_auto_20180917_0302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documentoadmitido',
            options={'ordering': ['admitido', 'fecha_creacion', 'fecha_edicion'], 'verbose_name': 'Documento Radicado', 'verbose_name_plural': 'Documentos Radicados'},
        ),
    ]
