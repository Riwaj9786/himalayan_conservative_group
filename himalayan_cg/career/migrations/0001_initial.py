# Generated by Django 5.1.3 on 2024-11-25 04:50

import ckeditor_uploader.fields
import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 11, 25, 4, 50, 45, 533830, tzinfo=datetime.timezone.utc))),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deadline', models.DateTimeField(default=datetime.datetime(2024, 12, 2, 4, 50, 45, 533830, tzinfo=datetime.timezone.utc))),
                ('position_name', models.CharField(max_length=255)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('position_type', models.CharField(blank=True, choices=[('Internship', 'Internship'), ('Entry Level', 'Entry Level'), ('Mid Level', 'Mid Level'), ('Senior Level', 'Senior Level')], max_length=40, null=True)),
                ('job_type', models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=40, null=True)),
                ('job_location', models.CharField(blank=True, choices=[('Remote', 'Remote'), ('Hybrid', 'Hybrid'), ('On-Site', 'On-Site')], max_length=40, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CareerApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55)),
                ('last_name', models.CharField(max_length=115)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.BigIntegerField()),
                ('cv', models.FileField(upload_to='careers/cv/<django.db.models.fields.related.ForeignKey>/')),
                ('accepted', models.BooleanField(default=False)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='apply_position', to='career.career')),
            ],
        ),
    ]