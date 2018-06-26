from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    age = models.PositiveIntegerField(
        verbose_name="Edad",
        min=13, max=125)

    gender = models.CharField(
        choices=['Femenino', 'Masculino'],
        verbose_name='Sexo',
        widget=widgets.RadioSelect())

    field = models.CharField(
        choices=['Economía', 'Psicología', "Derecho", "Ingeniería","Gestión y Alta Dirección","Arquitectura","Sociología","Ciencias políticas","Antropología","C. Comunicación","Humanidades", "Otra"],
        verbose_name='¿Qué carrera estudias?',
        widget=widgets.RadioSelect())

    tax1 = models.CharField(
        choices=['Sí', 'No'],
        verbose_name = '¿Es justificable pagar menores impuestos al Estado?',
        widget = widgets.RadioSelect())

    tax2 = models.CharField(
        choices=['Sí', 'No'],
        verbose_name = '¿Pagarías menores impuestos al Estado, sabiendo que la probabilidad de ser atrapado es mínima?',
        widget = widgets.RadioSelect())

    corrup = models.CharField(
        choices=['Sí', 'No'],
        verbose_name = '¿Crees que existe corrupción en el Estado?',
        widget = widgets.RadioSelect())

    malg = models.CharField(
        choices=['Sí', 'No'],
        verbose_name = '¿Crees que el Estado malgasta el dinero que recibe de los contribuyentes?',
        widget = widgets.RadioSelect())

    tasa1 = models.CharField(
        choices=['Sí', 'No'],
        verbose_name = '¿Es justificable que se aumente la tasa de impuestos si el Estado promete invertir el dinero en más obras para la población?',
        widget = widgets.RadioSelect())

    tasa2 = models.CharField(
        choices=['Sí', 'No'],
        verbose_name = 'De acuerdo con la pregunta anterior, ¿Estarías dispuesto a contribuir con mayores impuestos a pesar de que las obras y políticas del Estado no te beneficien directamente?',
        widget = widgets.RadioSelect())

    avrisk = models.CharField(
        choices=['Sí', 'No'],
        verbose_name = '¿Apostarías S/.10 si existe un 50% de probabilidad de que ganes S/.5 más pero 50% de probabilidad de que pierdas S/. 5?',
        widget = widgets.RadioSelect())

