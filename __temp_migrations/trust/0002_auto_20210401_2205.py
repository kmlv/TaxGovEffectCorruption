# Generated by Django 2.2.12 on 2021-04-02 03:05

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('trust', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='round_payoff',
            field=otree.db.models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='sent_amount',
            field=otree.db.models.CurrencyField(null=True),
        ),
    ]