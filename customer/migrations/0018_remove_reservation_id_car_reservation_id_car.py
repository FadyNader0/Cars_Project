# Generated by Django 5.1.4 on 2024-12-24 02:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_remove_reservation_id_car_reservation_id_car'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='id_car',
        ),
        migrations.AddField(
            model_name='reservation',
            name='id_car',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='customer.cars'),
            preserve_default=False,
        ),
    ]
