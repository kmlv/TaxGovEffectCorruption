# Generated by Django 2.2.12 on 2021-04-08 03:18

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatum', '0005_auto_20210406_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='response_0',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 0 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_10',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 10 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_100',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 100 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_20',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 20 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_30',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 30 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_40',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 40 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_50',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 50 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_60',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 60 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_70',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 70 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_80',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 80 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='response_90',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Acep    tarías una oferta de 90 Soles?'),
        ),
        migrations.AddField(
            model_name='group',
            name='use_strategy_method',
            field=otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True),
        ),
    ]
