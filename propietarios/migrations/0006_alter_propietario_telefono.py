# Generated by Django 4.2.9 on 2024-02-02 09:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("propietarios", "0005_alter_propietario_telefono"),
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
                        "^\\d{10}$", "Solo se permiten ingresar nros."
                    )
                ],
            ),
        ),
    ]
