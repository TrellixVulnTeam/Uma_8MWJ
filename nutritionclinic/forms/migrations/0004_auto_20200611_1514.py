# Generated by Django 2.0 on 2020-06-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20200611_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childreg',
            name='address_geolocate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='age_in_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='age_in_months',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='antenalvisit',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='anythingspecify',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='babybath',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='babytransfertotherhsptl',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='babyvaccine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='baseline_height',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='baseline_muac_mm',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='baseline_stntd_stats',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='baseline_uw_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='baseline_weight',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='baseline_wstng_stats',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='besidemilk',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='bfdone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='birth_length_in_cms',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='birth_weight',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='breastcrawlimmediatedone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='breastfeedathome',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='breastfeedskill',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='bywhom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='cause_deaths_sblngs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='child_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='cimage',
            field=models.ImageField(blank=True, null=True, upload_to='models/upload'),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='conditionatbirth',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='conditionofmother',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='date_of_reg',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='dctrprscribtn',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='discharge_weight',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='dob_last_child',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='father_height',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='fcontact_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='gestational',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='head_circumference_cm',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='holdduringbreastfeed',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='institution',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='kangaroocare',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='length_height_percentile',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='mcontact_no',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='mother_height',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='mother_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='mother_s_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='name_of_gynecologist',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='name_of_pediatrician',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='nmbrbrthrs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='nmbrsis',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='no_of_siblings',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='num_deaths_sblngs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='onlybrstmilk',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='othersspecify',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='presenceatdelivery',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='religion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='skintouchforhr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='specify9_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='specifyanyone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='specifycause',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='specifyothrs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='specifyplace',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='umbilicalcut',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='vitamink',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='weight_percentile',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='whatanythin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='childreg',
            name='whichvaccine',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
