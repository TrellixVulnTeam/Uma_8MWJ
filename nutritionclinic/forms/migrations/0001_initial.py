# Generated by Django 2.0 on 2020-06-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='breastfeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wash', models.CharField(max_length=10)),
                ('water', models.CharField(max_length=10)),
                ('sat', models.CharField(max_length=10)),
                ('back', models.CharField(max_length=10)),
                ('shldr', models.CharField(max_length=10)),
                ('uncvrd', models.CharField(max_length=10)),
                ('pressure', models.CharField(max_length=10)),
                ('unwrapped', models.CharField(max_length=10)),
                ('heldbaby', models.CharField(max_length=10)),
                ('legstucked', models.CharField(max_length=10)),
                ('elevatebaby', models.CharField(max_length=10)),
                ('thumb', models.CharField(max_length=10)),
                ('wrist', models.CharField(max_length=10)),
                ('babytummy', models.CharField(max_length=10)),
                ('head', models.CharField(max_length=10)),
                ('nose', models.CharField(max_length=10)),
                ('fullbody', models.CharField(max_length=10)),
                ('chin', models.CharField(max_length=10)),
                ('cupped', models.CharField(max_length=10)),
                ('finger', models.CharField(max_length=10)),
                ('distance', models.CharField(max_length=10)),
                ('parallel', models.CharField(max_length=10)),
                ('compressbaby', models.CharField(max_length=10)),
                ('equal', models.CharField(max_length=10)),
                ('avoid', models.CharField(max_length=10)),
                ('open', models.CharField(max_length=10)),
                ('mouth', models.CharField(max_length=10)),
                ('upperlips', models.CharField(max_length=10)),
                ('lowerlip', models.CharField(max_length=10)),
                ('latched', models.CharField(max_length=10)),
                ('chins', models.CharField(max_length=10)),
                ('lower', models.CharField(max_length=10)),
                ('fedfrombreast', models.CharField(max_length=10)),
                ('empty', models.CharField(max_length=10)),
                ('foremilk', models.CharField(max_length=10)),
                ('offer', models.CharField(max_length=10)),
                ('burped', models.CharField(max_length=10)),
                ('wokeup', models.CharField(max_length=10)),
                ('used', models.CharField(max_length=10)),
                ('hunger', models.CharField(max_length=10)),
                ('nosepressed', models.CharField(max_length=10)),
                ('latching', models.CharField(max_length=10)),
                ('brestfeedhrs', models.CharField(max_length=10)),
                ('bfnyt', models.CharField(max_length=10)),
                ('growth', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='childreg',
            fields=[
                ('date_of_reg', models.DateField(max_length=100)),
                ('child_id', models.IntegerField(primary_key=True, serialize=False)),
                ('child_name', models.CharField(max_length=100)),
                ('cimage', models.ImageField(upload_to='models/upload')),
                ('bd', models.DateField(blank=True, max_length=100, null=True)),
                ('age', models.IntegerField()),
                ('age_in_months', models.IntegerField()),
                ('age_in_days', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_s_age', models.IntegerField()),
                ('mother_height', models.DecimalField(decimal_places=5, max_digits=10)),
                ('mcontact_no', models.IntegerField()),
                ('father_height', models.DecimalField(decimal_places=5, max_digits=10)),
                ('fcontact_no', models.IntegerField()),
                ('address_geolocate', models.CharField(max_length=100)),
                ('no_of_siblings', models.IntegerField()),
                ('nmbrbrthrs', models.CharField(max_length=100)),
                ('nmbrsis', models.CharField(max_length=100)),
                ('num_deaths_sblngs', models.CharField(max_length=100)),
                ('cause_deaths_sblngs', models.CharField(max_length=100)),
                ('dob_last_child', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('name_of_gynecologist', models.CharField(max_length=100)),
                ('name_of_pediatrician', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('specifyothrs', models.CharField(max_length=100)),
                ('presenceatdelivery', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('gestational', models.CharField(max_length=100)),
                ('birth_weight', models.DecimalField(decimal_places=5, max_digits=10)),
                ('birth_length_in_cms', models.DecimalField(decimal_places=5, max_digits=10)),
                ('discharge_weight', models.DecimalField(decimal_places=5, max_digits=10)),
                ('conditionatbirth', models.CharField(max_length=100)),
                ('babytransfertotherhsptl', models.CharField(max_length=100)),
                ('specifycause', models.CharField(max_length=100)),
                ('breastcrawlimmediatedone', models.CharField(max_length=100)),
                ('bfdone', models.CharField(max_length=100)),
                ('umbilicalcut', models.CharField(max_length=100)),
                ('vitamink', models.CharField(max_length=100)),
                ('antenalvisit', models.CharField(max_length=100)),
                ('breastfeedskill', models.CharField(max_length=100)),
                ('bywhom', models.CharField(max_length=100)),
                ('othersspecify', models.CharField(max_length=100)),
                ('holdduringbreastfeed', models.CharField(max_length=100)),
                ('onlybrstmilk', models.CharField(max_length=100)),
                ('besidemilk', models.CharField(max_length=100)),
                ('whatanythin', models.CharField(max_length=100)),
                ('anythingspecify', models.CharField(max_length=100)),
                ('dctrprscribtn', models.CharField(max_length=100)),
                ('specifyanyone', models.CharField(max_length=100)),
                ('conditionofmother', models.CharField(max_length=100)),
                ('kangaroocare', models.CharField(max_length=100)),
                ('skintouchforhr', models.CharField(max_length=100)),
                ('specify9_name', models.CharField(max_length=100)),
                ('babybath', models.CharField(max_length=100)),
                ('babyvaccine', models.CharField(max_length=100)),
                ('whichvaccine', models.CharField(max_length=100)),
                ('breastfeedathome', models.CharField(max_length=100)),
                ('specifyplace', models.CharField(max_length=100)),
                ('baseline_weight', models.DecimalField(decimal_places=5, max_digits=10)),
                ('weight_percentile', models.DecimalField(decimal_places=5, max_digits=10)),
                ('baseline_height', models.DecimalField(decimal_places=5, max_digits=10)),
                ('length_height_percentile', models.DecimalField(decimal_places=5, max_digits=10)),
                ('head_circumference_cm', models.DecimalField(decimal_places=5, max_digits=10)),
                ('baseline_muac_mm', models.DecimalField(decimal_places=5, max_digits=10)),
                ('baseline_stntd_stats', models.CharField(max_length=100)),
                ('baseline_uw_status', models.CharField(max_length=100)),
                ('baseline_wstng_stats', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='immunizatn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=10)),
                ('cname', models.CharField(max_length=10)),
                ('measles', models.CharField(max_length=10)),
                ('optradio', models.CharField(max_length=10)),
                ('bcg', models.CharField(max_length=10)),
                ('hb', models.CharField(max_length=10)),
                ('opv', models.CharField(max_length=10)),
                ('opvweeks', models.CharField(max_length=10)),
                ('msls', models.CharField(max_length=10)),
                ('opvten', models.CharField(max_length=10)),
                ('rota', models.CharField(max_length=10)),
                ('vitmin', models.CharField(max_length=10)),
                ('rvirs', models.CharField(max_length=10)),
                ('opvforteen', models.CharField(max_length=10)),
                ('ipv', models.CharField(max_length=10)),
                ('mesls', models.CharField(max_length=10)),
                ('ipvweeks', models.CharField(max_length=10)),
                ('vitaminfiv', models.CharField(max_length=10)),
                ('pen', models.CharField(max_length=10)),
                ('opvboost', models.CharField(max_length=10)),
                ('thrdose', models.CharField(max_length=10)),
                ('dpt', models.CharField(max_length=10)),
                ('vitmina', models.CharField(max_length=10)),
                ('vitminafr', models.CharField(max_length=10)),
                ('vitminae8', models.CharField(max_length=10)),
                ('pentav', models.CharField(max_length=10)),
                ('vitamina2', models.CharField(max_length=10)),
                ('vitamina6', models.CharField(max_length=10)),
                ('pen14', models.CharField(max_length=10)),
                ('rota10', models.CharField(max_length=10)),
                ('vitamin7', models.CharField(max_length=10)),
            ],
        ),
    ]
