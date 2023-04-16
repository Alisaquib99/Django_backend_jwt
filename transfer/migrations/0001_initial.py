# Generated by Django 4.1.6 on 2023-04-15 19:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField(blank=True)),
                ('sent_type', models.BooleanField(default=True)),
                ('time', models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 15, 19, 4, 51, 521137, tzinfo=datetime.timezone.utc))),
                ('attach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
