# Generated by Django 5.1.2 on 2024-11-20 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carreras',
            fields=[
                ('idCarrera', models.AutoField(primary_key=True, serialize=False)),
                ('cveCarrera', models.CharField(max_length=10, unique=True)),
                ('nombreCarrera', models.CharField(max_length=255)),
                ('areaCarrera', models.CharField(max_length=30)),
                ('planEstudios', models.CharField(max_length=30)),
                ('bActivo', models.BooleanField(null=True)),
            ],
        ),
    ]