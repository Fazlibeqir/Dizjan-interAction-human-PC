# Generated by Django 5.0.3 on 2024-03-12 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_slika"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="meal_type",
            field=models.CharField(
                choices=[
                    ("IT", "Italian"),
                    ("CH", "Chinese"),
                    ("JA", "Japanese"),
                    ("ME", "Mexican"),
                ],
                max_length=255,
            ),
        ),
        migrations.CreateModel(
            name="Nagrada",
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
                    "chef",
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