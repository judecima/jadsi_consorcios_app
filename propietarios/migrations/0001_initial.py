# Generated by Django 4.2.9 on 2024-01-27 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Propietario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=250, null=True)),
                ("apellido", models.CharField(blank=True, max_length=250, null=True)),
                ("telefono", models.CharField(blank=True, max_length=250, null=True)),
                ("direccion", models.CharField(blank=True, max_length=250, null=True)),
                ("email", models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Lote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nro_lote", models.CharField(blank=True, max_length=250, null=True)),
                ("seccion", models.CharField(blank=True, max_length=250, null=True)),
                ("construccion", models.BooleanField(default=False)),
                ("aguado", models.BooleanField(default=False)),
                ("agua", models.BooleanField(default=False)),
                ("electricidad", models.BooleanField(default=False)),
                (
                    "Propietario",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="propietarios.propietario",
                    ),
                ),
            ],
        ),
    ]
