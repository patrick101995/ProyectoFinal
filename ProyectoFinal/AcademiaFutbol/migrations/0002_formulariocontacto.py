# Generated by Django 4.0.1 on 2022-01-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademiaFutbol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormularioContacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pnombre', models.CharField(max_length=40)),
                ('Snombre', models.CharField(max_length=40)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('comentarios', models.CharField(max_length=100)),
            ],
        ),
    ]
