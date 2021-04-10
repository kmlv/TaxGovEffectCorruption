from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import config_leex_1

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = models.Player
    form_fields = ['contribution']

    timeout_submission = {'contribution': c(Constants.endowment / 2)}


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Waiting for other participants to contribute."


class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(self):
        return {
            'total_earnings': self.group.total_contribution * Constants.multiplier,
        }

    def before_next_page(self):

        # pass payoff to new var
        self.player.round_payoff = self.player.payoff

        if config_leex_1.paid_game == Constants.name_in_url and config_leex_1.paid_round == self.round_number:
            self.player.payoff = self.player.payoff
        else:
            self.player.payoff = 0


page_sequence = [
    Introduction,
    Contribute,
    ResultsWaitPage,
    Results
]
