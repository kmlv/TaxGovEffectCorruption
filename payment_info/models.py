from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class Constants(BaseConstants):
    name_in_url = 'payment_info'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    
    def set_final_payoffs(self):
        """
        Choses a random app for paying the player

        Input: None
        Output: None
        """

        apps = self.session.config["app_sequence"][1:-2]

        print("app sequence without last app", apps)
        random.shuffle(apps)
        self.chosen_app = apps[0]
        self.participant.payoff = self.participant.vars["payoff_"+self.chosen_app]

    chosen_app = models.StringField()


