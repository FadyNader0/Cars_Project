# Generated by Django 5.1.4 on 2024-12-22 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_request_sold_price_sale_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='repairs',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('type_repair', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type_car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.cars')),
            ],
        ),
    ]
