# Generated by Django 2.2.12 on 2021-04-29 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('public_goods', '0004_subsession_chosen_app'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsession',
            name='chosen_app',
        ),
    ]
