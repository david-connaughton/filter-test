# Generated by Django 2.2 on 2020-12-08 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blog_image_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
