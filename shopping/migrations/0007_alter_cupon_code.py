# Generated by Django 3.2.5 on 2021-08-17 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_cupon_is_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupon',
            name='code',
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
    ]
