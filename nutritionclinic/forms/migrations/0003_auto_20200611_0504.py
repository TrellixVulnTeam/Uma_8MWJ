# Generated by Django 2.0 on 2020-06-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20200609_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childreg',
            name='fcontact_no',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='mcontact_no',
            field=models.BigIntegerField(),
        ),
    ]
