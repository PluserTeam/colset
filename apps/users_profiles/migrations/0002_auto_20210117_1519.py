# Generated by Django 3.1.3 on 2021-01-17 20:19

import apps.users_profiles.models
import config.extrafields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cv',
            field=config.extrafields.ContentTypeRestrictedFileField(blank=True, upload_to=apps.users_profiles.models.upload_dynamic_cv),
        ),
    ]
