# Generated by Django 3.0.3 on 2020-02-19 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_title',
        ),
    ]
