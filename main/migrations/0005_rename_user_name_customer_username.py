# Generated by Django 4.2.13 on 2024-06-29 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_energy_producer_delete_producer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='user_name',
            new_name='username',
        ),
    ]
