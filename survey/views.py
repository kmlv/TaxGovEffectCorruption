from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Demographics(Page):
    form_model = models.Player
    form_fields = ['age',
                   'gender',
                   'field']


class Tax(Page):
    form_model = models.Player
    form_fields = ['tax1',
                   'tax2',
                   'corrup',
                   "malg",
                   "tasa1",
                   "tasa2",
                   "avrisk"]


page_sequence = [
    Demographics,
    Tax
]
