# Generated by Django 2.2.12 on 2022-02-01 17:07

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('public_goods', '0002_auto_20220201_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='contribution',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='round_payoff',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]