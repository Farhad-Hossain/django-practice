# Generated by Django 4.0.7 on 2023-04-25 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0010_alter_person_email'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='person',
            name='Email must be unique',
        ),
    ]
