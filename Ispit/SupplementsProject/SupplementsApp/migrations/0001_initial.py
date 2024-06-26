# Generated by Django 5.0.6 on 2024-06-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='upload_to/')),
                ('code', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('price', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('proteins', 'proteins'), ('vitamins', 'vitamins'), ('amino acids', 'amino acids'), ('pre-workout', 'pre-workout')], max_length=50)),
            ],
        ),
    ]
