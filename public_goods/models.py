from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random, json
import config_leex_1


doc = """
This is a one-period public goods game with 3 players.
"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = 4
    num_rounds = 1
    contact_template =name_in_url + "/Contactenos.html"

    instructions_template = 'public_goods/Instructions.html'

    # """Amount allocated to each player"""
    endowment = config_leex_1.PG_endowment
    multiplier = 2


class Subsession(BaseSubsession):
#    chosen_app = models.StringField()

    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        else:
            self.group_like_round(1)

    def vars_for_admin_report(self):
        contributions = [p.contribution for p in self.get_players() if p.contribution != None]
        if contributions:
            return {
                'avg_contribution': sum(contributions)/len(contributions),
                'min_contribution': min(contributions),
                'max_contribution': max(contributions),
            }
        else:
            return {
                'avg_contribution': '(no data)',
                'min_contribution': '(no data)',
                'max_contribution': '(no data)',
            }

    # def set_final_payoffs(self):
    #     apps = self.session.config["app_sequence"][:-2]
    #     print("app sequence without last app", apps)
    #     random.shuffle(apps)
    #     self.chosen_app = apps[0]
    #     for p in self.get_players():
    #         p.participant.payoff = p.participant.vars["payoff_"+self.chosen_app]


class Group(BaseGroup):
    total_contribution = models.IntegerField()
    individual_share = models.FloatField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.multiplier / Constants.players_per_group
        for p in self.get_players():
            p.payoff = (Constants.endowment - p.contribution) + self.individual_share


class Player(BasePlayer):
    contribution = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    round_payoff = models.CurrencyField()

    def role(self):
        if self.id_in_group == 1:
            return 'A'
        elif self.id_in_group == 2:
            return 'B'
        elif self.id_in_group == 3:
            return 'C'
        else:
            return 'D'