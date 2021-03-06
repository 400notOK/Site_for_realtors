# Generated by Django 2.2.4 on 2020-05-01 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0004_auto_20200501_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_description', models.TextField(blank=True, max_length=400, verbose_name='Текст жалобы')),
                ('report_flat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Flat')),
                ('report_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
