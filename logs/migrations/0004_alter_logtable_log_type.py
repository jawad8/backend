# Generated by Django 4.0.6 on 2022-07-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0003_alter_logtable_log_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logtable',
            name='log_type',
            field=models.IntegerField(choices=[(0, 'not_set'), (20, 'info'), (40, 'error'), (10, 'debug'), (50, 'critical'), (30, 'warning')]),
        ),
    ]
