# Generated by Django 3.0.3 on 2020-07-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ida_core', '0009_auto_20200727_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectgroup',
            old_name='data',
            new_name='dataset_families',
        ),
    ]
