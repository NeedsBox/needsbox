# Generated by Django 3.1.6 on 2021-02-15 16:23

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_small_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', phone_field.models.PhoneField(max_length=31, null=True)),
                ('address', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
