# Generated by Django 2.2.4 on 2020-05-01 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_report'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='report_flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Flat', verbose_name='Квартира, на которую жаловались'),
        ),
        migrations.AlterField(
            model_name='report',
            name='report_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
