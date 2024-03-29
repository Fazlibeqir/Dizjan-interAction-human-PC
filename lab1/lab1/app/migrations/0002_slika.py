# Generated by Django 5.0.3 on 2024-03-12 18:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Slika",
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
                (
                    "gotvac",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.gotvac"
                    ),
                ),
                (
                    "recept",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.recept"
                    ),
                ),
            ],
        ),
    ]
