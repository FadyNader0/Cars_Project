# Generated by Django 5.1.4 on 2024-12-24 02:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_alter_request_sold_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id_car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='customer.cars'),
        ),
    ]
