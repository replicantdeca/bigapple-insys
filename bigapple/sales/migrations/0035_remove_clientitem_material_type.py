# Generated by Django 2.0.6 on 2018-07-17 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0034_auto_20180717_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientitem',
            name='material_type',
        ),
    ]
