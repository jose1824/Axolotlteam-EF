# Generated by Django 3.0.5 on 2021-02-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20210220_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ubications',
            name='altitud',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Altitud'),
        ),
        migrations.AlterField(
            model_name='ubications',
            name='latitud',
            field=models.DecimalField(decimal_places=100, max_digits=1000, verbose_name='Latitud'),
        ),
    ]
