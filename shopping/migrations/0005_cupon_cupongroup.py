# Generated by Django 3.2.5 on 2021-08-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210805_0647'),
        ('shopping', '0004_auto_20210805_0702'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuponGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('stock', models.FloatField()),
                ('expires_in', models.DateTimeField()),
                ('category', models.ManyToManyField(to='store.SubCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=8)),
                ('stock', models.FloatField()),
                ('expires_in', models.DateTimeField()),
                ('category', models.ManyToManyField(to='store.SubCategory')),
            ],
        ),
    ]
