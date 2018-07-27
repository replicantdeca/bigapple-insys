# Generated by Django 2.0.6 on 2018-06-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0004_auto_20180626_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='department',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_type',
            field=models.CharField(choices=[('Raw Material', 'Raw Material'), ('Machinery/Parts', 'Machinery/Parts'), ('Ink', 'Ink'), ('Others', 'Others')], default='not specified', max_length=200, verbose_name='suppier_type'),
        ),
    ]
