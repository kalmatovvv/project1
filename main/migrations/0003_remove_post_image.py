# Generated by Django 3.1 on 2021-04-04 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]