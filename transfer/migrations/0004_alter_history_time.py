# Generated by Django 4.1.6 on 2023-04-15 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0003_alter_history_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 19, 37, 3, 458193, tzinfo=datetime.timezone.utc)),
        ),
    ]
