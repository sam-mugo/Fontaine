# Generated by Django 3.2.8 on 2021-12-08 15:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_blog', '0007_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
