# Generated by Django 2.0.6 on 2018-06-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_mgt', '0003_auto_20180626_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientitem',
            name='laminate',
            field=models.BooleanField(default=True, verbose_name='laminate'),
        ),
    ]
