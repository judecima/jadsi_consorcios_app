# Generated by Django 4.2.9 on 2024-02-02 09:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("propietarios", "0004_multa_monto_multa_resolucion"),
    ]

    operations = [
        migrations.AlterField(
            model_name="propietario",
            name="telefono",
            field=models.CharField(
                blank=True,
                max_length=10,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^\\\\d+$", "Solo se permiten ingresar nros."
                    )
                ],
            ),
        ),
    ]
