# Generated by Django 2.2.12 on 2021-06-28 04:58

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('trust', '0003_auto_20210627_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sent_amount_strategy',
            field=otree.db.models.CurrencyField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='¿Cuánto enviarías al Jugador B?'),
        ),
    ]