# Generated by Django 4.0.1 on 2022-01-24 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcademiaFutbol', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulariocontacto',
            old_name='Pnombre',
            new_name='pNombre',
        ),
        migrations.RenameField(
            model_name='formulariocontacto',
            old_name='Snombre',
            new_name='sNombre',
        ),
    ]
