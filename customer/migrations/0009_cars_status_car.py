# Generated by Django 5.1.4 on 2024-12-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_reservation_statues'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='status_car',
            field=models.BooleanField(default=True),
        ),
    ]