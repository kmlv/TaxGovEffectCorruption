from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        
        yield pages.Survey, {
            'punish_your_punisher': 10,
                   'punish_others_punisher': 3,
                   'donate_without_reward': 7,
                   'reciprocity': 10,
                   'revenge': 4,
                   'stranger_payback': 3
        }
