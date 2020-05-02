# Generated by Django 2.2.4 on 2020-05-02 10:56

from django.db import migrations
import phonenumbers


def normalize_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        normalize_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if not phonenumbers.is_valid_number(normalize_number):
            return
        flat.owner_phone_pure = phonenumbers.format_number(
            normalize_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(normalize_phonenumbers)
    ]
