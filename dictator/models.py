from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
One player decides how to divide a certain amount between himself and the other
player.

See: Kahneman, Daniel, Jack L. Knetsch, and Richard H. Thaler. "Fairness
and the assumptions of economics." Journal of business (1986):
S285-S300.

"""


class Constants(BaseConstants):
    name_in_url = 'dictator'
    players_per_group = 2
    num_rounds = 1
    id_random_dictator = random.randint(1, players_per_group)

    instructions_template = 'dictator/Instructions.html'

    # Initial amount allocated to the dictator
    endowment = c(100)


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):

    group_kept = models.CurrencyField(
            doc="""Amount actual dictator decided to keep for himself""",
            min=0, max=Constants.endowment)

    def set_random_dictator(self):
        """
        Sets randomly who will be selected as the dictator

        Input: None
        Output: None
        """
        
        for p in self.get_players():
            if p.id_in_group == Constants.id_random_dictator:
                p.dictator = True

    def set_group_data(self):
        """
        Sets group variables values

        Input: None
        Output: None
        """
        for p in self.get_players():
            if p.dictator:
                self.group_kept = p.kept

    def set_payoffs(self):
        """
        Sets the payoffs for each member of a group

        Input: None
        Output: None
        """
        amount_kept_dictator = 0 # storing dictator's decision
        
        # setting the payoffs for dictator in group
        for p in self.get_players():
            if p.dictator:
                amount_kept_dictator = p.kept
                p.payoff = amount_kept_dictator
            
        # looping again for setting non dictator's payoffs (cant assign before knowing who is dictator)
        for p in self.get_players():
            if not p.dictator:
                p.payoff = amount_kept_dictator
            

class Player(BasePlayer):
    kept = models.CurrencyField(
        doc="""Amount tentative dictator decided to keep for himself""",
        min=0, max=Constants.endowment,
        verbose_name='Si fueras el Participante 1, te quedarías con (desde 0 hasta %i)' % Constants.endowment
    )

    dictator = models.BooleanField(initial=False)

