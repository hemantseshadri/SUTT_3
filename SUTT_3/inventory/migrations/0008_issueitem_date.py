# Generated by Django 3.2.5 on 2022-06-05 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20220605_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='issueitem',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
