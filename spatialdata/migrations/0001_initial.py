# Generated by Django 3.1.5 on 2021-02-07 00:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Limits',
            fields=[
                ('concelho', models.CharField(max_length=254)),
                ('nome', models.CharField(max_length=254)),
                ('distrito', models.CharField(max_length=254)),
                ('distrito_title', models.CharField(max_length=254)),
                ('nuti', models.CharField(max_length=254)),
                ('nutii', models.CharField(max_length=254)),
                ('nutiii', models.CharField(max_length=254)),
                ('ilha', models.CharField(max_length=254, null=True)),
                ('ilha_title', models.CharField(max_length=27, null=True)),
                ('layer', models.CharField(max_length=100, null=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]