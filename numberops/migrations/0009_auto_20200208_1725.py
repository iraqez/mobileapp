# Generated by Django 3.0.2 on 2020-02-08 15:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('numberops', '0008_auto_20200208_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationsnum',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 8, 17, 25, 39, 552446)),
        ),
    ]