# Generated by Django 5.1 on 2024-08-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tolov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mijoz', models.CharField(max_length=120)),
                ('qolgan_butulkalar', models.SmallIntegerField()),
                ('kol_bo_suv', models.SmallIntegerField()),
                ('maxsulot', models.CharField(max_length=100)),
                ('naqt', models.FloatField()),
                ('plastik', models.FloatField()),
                ('chiqim', models.FloatField()),
                ('sana', models.DateField()),
            ],
        ),
    ]
