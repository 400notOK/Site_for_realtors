# Generated by Django 2.2.4 on 2020-05-01 16:35

from django.db import migrations


def checking_new_flat(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        if flat.construction_year > 2016:
            flat.new_building = True
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(checking_new_flat)
    ]
