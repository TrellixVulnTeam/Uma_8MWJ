# Generated by Django 2.0 on 2020-06-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0004_auto_20200611_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='immunizatn',
            name='optradio',
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='avoid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='babytummy',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='back',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='bfnyt',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='brestfeedhrs',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='burped',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='chin',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='chins',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='compressbaby',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='cupped',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='distance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='elevatebaby',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='empty',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='equal',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='fedfrombreast',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='finger',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='foremilk',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='fullbody',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='growth',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='head',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='heldbaby',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='hunger',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='latched',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='latching',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='legstucked',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='lower',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='lowerlip',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='mouth',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='nose',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='nosepressed',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='offer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='open',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='parallel',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='pressure',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='sat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='shldr',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='thumb',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='uncvrd',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='unwrapped',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='upperlips',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='used',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='wash',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='water',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='wokeup',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='breastfeed',
            name='wrist',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='bcg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='cid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='cname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='dpt',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='hb',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='ipv',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='ipvweeks',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='measles',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='mesls',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='msls',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='opv',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='opvboost',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='opvforteen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='opvten',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='opvweeks',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='pen',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='pen14',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='pentav',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='rota',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='rota10',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='rvirs',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='thrdose',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='vitamin7',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='vitamina2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='vitamina6',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='vitaminfiv',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='vitmin',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='vitmina',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='vitminae8',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='immunizatn',
            name='vitminafr',
            field=models.CharField(max_length=100),
        ),
    ]
