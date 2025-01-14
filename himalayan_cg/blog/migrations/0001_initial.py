# Generated by Django 5.1.3 on 2024-11-29 05:24

import ckeditor_uploader.fields
import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserProfile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
            },
        ),
        migrations.CreateModel(
            name='InitiativeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Initiative Category',
                'verbose_name_plural': 'Initiative Categories',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=60)),
                ('short_description', models.CharField(max_length=255)),
                ('introduction', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('conclusion', ckeditor_uploader.fields.RichTextUploadingField()),
                ('read_time', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_author', to='UserProfile.profile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_category', to='blog.blogcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeaturedBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_blog_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='feature_blog_1', to='blog.blog')),
                ('featured_blog_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='feature_blog_2', to='blog.blog')),
                ('featured_blog_3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='feature_blog_3', to='blog.blog')),
                ('featured_blog_4', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='feature_blog_4', to='blog.blog')),
            ],
        ),
        migrations.CreateModel(
            name='Initiatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('title', models.CharField(max_length=60)),
                ('short_description', models.CharField(max_length=255)),
                ('introduction', ckeditor_uploader.fields.RichTextUploadingField()),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('conclusion', ckeditor_uploader.fields.RichTextUploadingField()),
                ('read_time', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='initiative_author', to='UserProfile.profile')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='initiative_category', to='blog.initiativecategory')),
            ],
            options={
                'verbose_name': 'Initiative',
                'verbose_name_plural': 'Initiatives',
            },
        ),
        migrations.CreateModel(
            name='FeaturedInitiatives',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_initiative_1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featured_initiative_1', to='blog.initiatives')),
                ('featured_initiative_2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featured_initiative_2', to='blog.initiatives')),
                ('featured_initiative_3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featured_initiative_3', to='blog.initiatives')),
                ('featured_initiative_4', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='featured_initiative_4', to='blog.initiatives')),
            ],
        ),
    ]
