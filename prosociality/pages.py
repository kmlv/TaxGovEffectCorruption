from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Survey(Page):
    form_model = 'player'
    form_fields = ['punish_your_punisher',
                   'punish_others_punisher',
                   'donate_without_reward',
                   'reciprocity',
                   'revenge',
                   'stranger_payback']

page_sequence = [Survey]
