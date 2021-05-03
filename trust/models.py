from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random, json

import config_leex_1

doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'trust/Instructions.html'

    # Initial amount allocated to each player
    endowment = 10
    multiplication_factor = 3

    # Strategy method
    choice_step = 1 
    choices_trustor = [choice for choice in range(0, endowment+1, choice_step)]


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""Amount sent by P1""",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""",
        min=c(0),
    )

    # def set_random_trustor(self):
    #     """
    #     Sets randomly who will be selected as the trustor

    #     Input: None
    #     Output: None
    #     """
    #     id_random_trustor = random.randint(0, Constants.players_per_group)
    #     for p in self.get_players():
    #         if p.id_in_group == id_random_trustor:
    #             p.trustor = True
    #         else:
    #             p.trustee = True

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if self.session.config["use_strategy_method"] is False:
            p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
            p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount
        else:
            if p1.sent_amount_strategy == 0:
                p1.payoff = Constants.endowment
                p2.payoff = 0
                self.sent_back_amount = 0
            elif p1.sent_amount_strategy == 1:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_3
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_3
                self.sent_back_amount = p2.sent_back_amount_strategy_3
            elif p1.sent_amount_strategy == 2:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_6
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_6
                self.sent_back_amount = p2.sent_back_amount_strategy_6
            elif p1.sent_amount_strategy == 3:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_9
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_9
                self.sent_back_amount = p2.sent_back_amount_strategy_9
            elif p1.sent_amount_strategy == 4:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_12
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_12
                self.sent_back_amount = p2.sent_back_amount_strategy_12
            elif p1.sent_amount_strategy == 5:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_15
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_15
                self.sent_back_amount = p2.sent_back_amount_strategy_15
            elif p1.sent_amount_strategy == 6:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_18
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_18
                self.sent_back_amount = p2.sent_back_amount_strategy_18
            elif p1.sent_amount_strategy == 7:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_21
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_21
                self.sent_back_amount = p2.sent_back_amount_strategy_21
            elif p1.sent_amount_strategy == 8:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_24
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_24
                self.sent_back_amount = p2.sent_back_amount_strategy_24
            elif p1.sent_amount_strategy == 9:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_27
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_27
                self.sent_back_amount = p2.sent_back_amount_strategy_27
            elif p1.sent_amount_strategy == 10:
                p1.payoff = Constants.endowment - p1.sent_amount_strategy + p2.sent_back_amount_strategy_30
                p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - p2.sent_back_amount_strategy_30
                self.sent_back_amount = p2.sent_back_amount_strategy_30

    def set_group_data(self):
        for p in self.get_players():
            if p.role() == 'A':
                self.sent_amount = p.sent_amount_strategy
    

# function for strategy method fields (trustee)
def make_sent_back_field(received_amount):
    return models.IntegerField(
    choices=[choice for choice in range(received_amount + 1)],
    label=f"Si fueras el jugador B y recibieras {received_amount} puntos, ¿cuánto enviarías de vuelta al Jugador A?",
    #widget=widgets.RadioSelect,
)

class Player(BasePlayer):

    round_payoff = models.CurrencyField()

    # strategy method fields
    ## for trustor
    trustor = models.BooleanField(initial=False)
    sent_amount_strategy = models.CurrencyField(
            min=0, max=Constants.endowment,
            choices=Constants.choices_trustor,
            verbose_name="""Si fueras el jugador A, ¿cuánto enviarías al Jugador B?""",
        )

    ## for trustee
    trustee = models.BooleanField(initial=False)

    sent_back_amount_strategy_3 = make_sent_back_field(3)
    sent_back_amount_strategy_6 = make_sent_back_field(6)
    sent_back_amount_strategy_9 = make_sent_back_field(9)
    sent_back_amount_strategy_12 = make_sent_back_field(12)
    sent_back_amount_strategy_15 = make_sent_back_field(15)
    sent_back_amount_strategy_18 = make_sent_back_field(18)
    sent_back_amount_strategy_21 = make_sent_back_field(21)
    sent_back_amount_strategy_24 = make_sent_back_field(24)
    sent_back_amount_strategy_27 = make_sent_back_field(27)
    sent_back_amount_strategy_30 = make_sent_back_field(30)    

    def role(self):
        return {1: 'A', 2: 'B'}[self.id_in_group]
