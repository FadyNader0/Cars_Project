# Generated by Django 5.1.4 on 2024-12-22 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_repairs_type_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='repairs',
            name='image',
            field=models.ImageField(null=True, upload_to='image/%Y-%m-%d'),
        ),
    ]