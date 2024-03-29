# Generated by Django 4.2.9 on 2024-01-27 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("nombre", models.CharField(max_length=100)),
                ("numero_lote", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="ExpensaMensual",
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
                ("fecha", models.DateField()),
                ("monto", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "lote",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="expensas.lote"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Expensa",
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
                ("monto_a_pagar", models.DecimalField(decimal_places=2, max_digits=10)),
                ("pagado", models.BooleanField(default=False)),
                (
                    "mes",
                    models.DateField(
                        default=datetime.date.today, verbose_name="Mes de la Expensa"
                    ),
                ),
                (
                    "lote",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="expensas.lote"
                    ),
                ),
            ],
        ),
    ]
