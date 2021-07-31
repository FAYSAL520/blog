# Generated by Django 3.2.5 on 2021-07-30 21:08

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogsCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogscategory')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_short_description', models.TextField(max_length=500)),
                ('blog_image', models.ImageField(default='', upload_to='blogs/images')),
                ('blog_desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('views', models.IntegerField(default=0)),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogscategory')),
                ('blog_subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogsubcategory')),
            ],
        ),
    ]