# Generated by Django 2.0.6 on 2018-07-17 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_mgt', '0005_auto_20180714_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialRequisitionItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('to_be_used_for', models.CharField(max_length=200, verbose_name='to_be_used_for')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.Inventory')),
            ],
        ),
        migrations.RemoveField(
            model_name='materialrequisition',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='materialrequisition',
            name='description',
        ),
        migrations.RemoveField(
            model_name='materialrequisition',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='materialrequisition',
            name='to_be_used_for',
        ),
        migrations.AlterField(
            model_name='materialrequisition',
            name='date_issued',
            field=models.DateField(auto_now_add=True, verbose_name='date_issued'),
        ),
        migrations.AlterField(
            model_name='materialrequisition',
            name='issued_to',
            field=models.CharField(max_length=200, null=True, verbose_name='issued_to'),
        ),
        migrations.AddField(
            model_name='materialrequisitionitems',
            name='matreq',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_mgt.MaterialRequisition'),
        ),
    ]
