# Generated by Django 5.1.1 on 2024-09-13 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
