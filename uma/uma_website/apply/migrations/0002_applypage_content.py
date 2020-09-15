# Generated by Django 2.2.10 on 2020-05-22 13:26

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applypage',
            name='content',
            field=wagtail.core.fields.StreamField([('doc_upload', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('points', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('point', wagtail.core.blocks.CharBlock(max_length=200, required=True)), ('doc_upload', wagtail.documents.blocks.DocumentChooserBlock(required=True))])))]))], blank=True, null=True),
        ),
    ]
