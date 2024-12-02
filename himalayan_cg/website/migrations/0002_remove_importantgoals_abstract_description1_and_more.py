# Generated by Django 5.1.3 on 2024-12-02 04:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importantgoals',
            name='abstract_description1',
        ),
        migrations.RemoveField(
            model_name='importantgoals',
            name='abstract_description2',
        ),
        migrations.RemoveField(
            model_name='importantgoals',
            name='abstract_description3',
        ),
        migrations.RemoveField(
            model_name='importantgoals',
            name='icon1',
        ),
        migrations.RemoveField(
            model_name='importantgoals',
            name='icon2',
        ),
        migrations.RemoveField(
            model_name='importantgoals',
            name='icon3',
        ),
        migrations.RemoveField(
            model_name='importantgoals',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='importantgoals',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='importantgoals',
            name='title3',
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='icons/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])])),
                ('title', models.CharField(max_length=255)),
                ('abstract_description', models.TextField()),
                ('important_goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='website.importantgoals')),
            ],
        ),
    ]