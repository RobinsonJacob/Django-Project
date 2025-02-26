# Generated by Django 5.0.3 on 2024-03-18 05:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_deatails', '0004_rename_address_vendor_address_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='address_id',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='contact_deatails_id',
            new_name='contact_deatails',
        ),
        migrations.AlterField(
            model_name='vendor',
            name='status',
            field=models.SmallIntegerField(default=django.utils.timezone.now),
        ),
    ]
