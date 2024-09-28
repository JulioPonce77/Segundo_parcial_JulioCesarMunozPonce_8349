# Generated by Django 5.1.1 on 2024-09-28 21:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=10)),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.profesor')),
            ],
        ),
    ]
