# Generated by Django 2.2.10 on 2020-03-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20200129_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='tdsc',
            field=models.TextField(blank=True, default='TDSC', null=True),
        ),
    ]
