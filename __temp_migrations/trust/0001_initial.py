# Generated by Django 2.2.12 on 2021-06-09 23:18

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('sent_amount', otree.db.models.CurrencyField(null=True)),
                ('sent_back_amount', otree.db.models.CurrencyField(null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trust_group', to='otree.Session')),
            ],
            options={
                'db_table': 'trust_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trust_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'trust_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('round_payoff', otree.db.models.CurrencyField(null=True)),
                ('trustor', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('sent_amount_strategy', otree.db.models.CurrencyField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Si fueras el jugador A, ¿cuánto enviarías al Jugador B?')),
                ('trustee', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('sent_back_amount_strategy_3', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], null=True, verbose_name='Si fueras el jugador B y recibieras 3 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_6', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True, verbose_name='Si fueras el jugador B y recibieras 6 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_9', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)], null=True, verbose_name='Si fueras el jugador B y recibieras 9 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_12', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], null=True, verbose_name='Si fueras el jugador B y recibieras 12 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_15', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)], null=True, verbose_name='Si fueras el jugador B y recibieras 15 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_18', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18)], null=True, verbose_name='Si fueras el jugador B y recibieras 18 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_21', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21)], null=True, verbose_name='Si fueras el jugador B y recibieras 21 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_24', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)], null=True, verbose_name='Si fueras el jugador B y recibieras 24 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_27', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)], null=True, verbose_name='Si fueras el jugador B y recibieras 27 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('sent_back_amount_strategy_30', otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], null=True, verbose_name='Si fueras el jugador B y recibieras 30 puntos, ¿cuánto enviarías de vuelta al Jugador A?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trust.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trust_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trust_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trust.Subsession')),
            ],
            options={
                'db_table': 'trust_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trust.Subsession'),
        ),
    ]
