# Generated by Django 3.2.4 on 2021-08-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0007_alter_cupon_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='reduced_price',
            field=models.FloatField(blank=True, default=0.0),
        ),
    ]
