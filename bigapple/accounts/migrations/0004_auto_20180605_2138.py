# Generated by Django 2.1a1 on 2018-06-05 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_mgt', '0003_auto_20180603_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='accounts',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts_mgt.Account'),
        ),
    ]
