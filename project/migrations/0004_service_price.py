# Generated by Django 3.1.6 on 2021-02-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20210212_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
