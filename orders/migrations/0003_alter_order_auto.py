# Generated by Django 5.1 on 2024-08-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='auto',
            field=models.CharField(max_length=100),
        ),
    ]
