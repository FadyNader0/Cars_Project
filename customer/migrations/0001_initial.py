# Generated by Django 5.1.4 on 2024-12-22 03:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('manufacture_date', models.DateField()),
                ('status', models.CharField(choices=[('used', 'used'), ('new', 'new')], max_length=5)),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('price_reserv', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('kilo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/%Y-%m-%d')),
                ('stock', models.IntegerField()),
                ('reserv', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='drivers',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='request_sold',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_customer', models.CharField(max_length=20)),
                ('cust_name', models.CharField(max_length=20)),
                ('name_car', models.CharField(max_length=50)),
                ('type_car', models.CharField(max_length=50)),
                ('manufacture_date_car', models.DateField()),
                ('price_sale_car', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kilo_car', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color_car', models.CharField(max_length=100)),
                ('image_car', models.ImageField(upload_to='image/%Y-%m-%d')),
                ('statues', models.CharField(choices=[('Confirm', 'Confirm'), ('Refuse', 'Refuse')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='cars_bought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_id', models.CharField(max_length=20)),
                ('cust_name', models.CharField(max_length=30)),
                ('cust_phone', models.IntegerField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.cars')),
            ],
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_cust', models.IntegerField()),
                ('cust_name', models.CharField(max_length=20)),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_car', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='customer.cars')),
                ('id_driver', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customer.drivers')),
            ],
        ),
    ]
