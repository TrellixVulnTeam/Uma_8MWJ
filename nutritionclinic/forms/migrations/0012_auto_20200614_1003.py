# Generated by Django 2.0 on 2020-06-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_auto_20200614_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childreg',
            name='cimage',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
