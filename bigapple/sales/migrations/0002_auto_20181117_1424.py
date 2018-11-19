# Generated by Django 2.1.3 on 2018-11-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoice',
            name='date_issued',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='salesinvoice',
            name='total_paid',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
