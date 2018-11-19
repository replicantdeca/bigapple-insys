# Generated by Django 2.1.3 on 2018-11-17 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joborder',
            name='status',
            field=models.CharField(choices=[('Waiting', 'Waiting'), ('On Queue', 'On Queue'), ('Under Cutting', 'Under Cutting'), ('Under Extrusion', 'Under Extrusion'), ('Under Printing', 'Under Printing'), ('Under Laminating', 'Under Laminating'), ('Under Packaging', 'Under Packaging'), ('Ready for delivery', 'Ready for delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Waiting', max_length=200, verbose_name='status'),
        ),
    ]
