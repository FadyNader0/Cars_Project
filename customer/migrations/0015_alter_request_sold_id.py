# Generated by Django 5.1.4 on 2024-12-24 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_alter_request_sold_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_sold',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
