# Generated by Django 4.2.9 on 2024-01-27 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("propietarios", "0002_alter_lote_nro_lote_alter_propietario_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Multa",
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
                (
                    "descripcion",
                    models.TextField(blank=True, max_length=250, null=True),
                ),
                (
                    "Propietario",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="propietarios.propietario",
                    ),
                ),
                (
                    "afectados",
                    models.ManyToManyField(
                        related_name="afectados_multas", to="propietarios.propietario"
                    ),
                ),
            ],
        ),
    ]
