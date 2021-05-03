# Generated by Django 2.2.12 on 2021-03-01 23:56

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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_group', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='survey_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'survey_subsession',
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
                ('age', otree.db.models.PositiveIntegerField(null=True, verbose_name='Edad')),
                ('gender', otree.db.models.StringField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], max_length=10000, null=True, verbose_name='Sexo')),
                ('field', otree.db.models.StringField(choices=[('Economía', 'Economía'), ('Psicología', 'Psicología'), ('Derecho', 'Derecho'), ('Ingeniería', 'Ingeniería'), ('Gestión y Alta Dirección', 'Gestión y Alta Dirección'), ('Arquitectura', 'Arquitectura'), ('Sociología', 'Sociología'), ('Ciencias políticas', 'Ciencias políticas'), ('Antropología', 'Antropología'), ('C. Comunicación', 'C. Comunicación'), ('Humanidades', 'Humanidades'), ('Otra', 'Otra')], max_length=10000, null=True, verbose_name='¿Qué carrera estudias?')),
                ('tax1', otree.db.models.StringField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=10000, null=True, verbose_name='¿Es justificable pagar menores impuestos al Estado?')),
                ('tax2', otree.db.models.StringField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=10000, null=True, verbose_name='¿Pagarías menores impuestos al Estado, sabiendo que la probabilidad de ser atrapado es mínima?')),
                ('corrup', otree.db.models.StringField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=10000, null=True, verbose_name='¿Crees que existe corrupción en el Estado?')),
                ('malg', otree.db.models.StringField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=10000, null=True, verbose_name='¿Crees que el Estado malgasta el dinero que recibe de los contribuyentes?')),
                ('tasa1', otree.db.models.StringField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=10000, null=True, verbose_name='¿Es justificable que se aumente la tasa de impuestos si el Estado promete invertir el dinero en más obras para la población?')),
                ('tasa2', otree.db.models.StringField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=10000, null=True, verbose_name='De acuerdo con la pregunta anterior, ¿Estarías dispuesto a contribuir con mayores impuestos a pesar de que las obras y políticas del Estado no te beneficien directamente?')),
                ('avrisk', otree.db.models.StringField(choices=[('Sí', 'Sí'), ('No', 'No')], max_length=10000, null=True, verbose_name='¿Apostarías S/.10 si existe un 50% de probabilidad de que ganes S/.5 más pero 50% de probabilidad de que pierdas S/. 5?')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='survey_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Subsession')),
            ],
            options={
                'db_table': 'survey_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.Subsession'),
        ),
    ]
