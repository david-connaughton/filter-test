# Generated by Django 2.2 on 2020-12-26 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20201226_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
