# Generated by Django 3.2.4 on 2021-08-20 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gmail',
            new_name='email',
        ),
    ]
