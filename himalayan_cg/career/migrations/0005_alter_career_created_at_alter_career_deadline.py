# Generated by Django 5.1.3 on 2024-11-25 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("career", "0004_alter_career_created_at_alter_career_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="career",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 11, 25, 14, 25, 44, 856494, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="career",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 12, 2, 14, 25, 44, 856494, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]