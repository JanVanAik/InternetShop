# Generated by Django 4.2.9 on 2024-02-05 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_activation_key_user_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_expires',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 2, 7, 18, 5, 57, 637576, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
