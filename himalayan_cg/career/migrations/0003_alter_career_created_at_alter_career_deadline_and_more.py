# Generated by Django 5.1.3 on 2024-11-25 05:14

import career.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_rename_is_active_career__is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 25, 5, 14, 37, 317196, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='career',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 2, 5, 14, 37, 317196, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='careerapply',
            name='cv',
            field=models.FileField(upload_to=career.models.upload_to_cv),
        ),
    ]
