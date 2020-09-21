# Generated by Django 3.1.1 on 2020-09-21 08:24

from django.db import migrations
import pdm.models


class Migration(migrations.Migration):

    dependencies = [
        ('pdm', '0002_auto_20200920_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterparty',
            name='email',
            field=pdm.models.NullableEmailField(blank=True, default=None, max_length=254, null=True, unique=True, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='product',
            name='part_number',
            field=pdm.models.NullableCharField(blank=True, default=None, max_length=50, null=True, unique=True, verbose_name='part_number'),
        ),
    ]