# Generated by Django 4.0.7 on 2023-04-25 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0011_remove_person_email must be unique'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='person',
            name='age_constraint',
        ),
    ]
