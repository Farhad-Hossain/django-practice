# Generated by Django 3.2.12 on 2023-04-21 11:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_auto_20230421_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='date_joined',
            field=models.DateField(default=datetime.date(1900, 1, 1)),
        ),
    ]