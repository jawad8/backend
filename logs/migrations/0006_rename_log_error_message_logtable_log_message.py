# Generated by Django 4.0.6 on 2022-07-20 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0005_alter_logtable_log_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logtable',
            old_name='log_error_Message',
            new_name='log_message',
        ),
    ]
