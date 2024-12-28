# Generated by Django 5.1.4 on 2024-12-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_alter_reservation_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
