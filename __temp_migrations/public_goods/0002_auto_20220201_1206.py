# Generated by Django 2.2.12 on 2022-02-01 17:06

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('public_goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='individual_share',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='total_contribution',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
