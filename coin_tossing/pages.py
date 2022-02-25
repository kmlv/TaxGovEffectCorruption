from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.participant.vars["payoff_"+Constants.name_app] = 0


class TossingTheCoin(Page):
    timeout_seconds = 2


class Report(Page):
    form_model = "player"
    form_fields = ["heads_or_tails"]

    def vars_for_template(self):
        return {"real_coin_value": self.player.real_coin_value,
                "guess": self.player.heads_or_tails}

    def before_next_page(self):
        if self.player.heads_or_tails == Constants.head_value:
            self.player.number_of_heads += 1
            self.player.payoff += Constants.head_payment
            self.player.participant.vars["payoff_"+Constants.name_app] += self.player.payoff
        
        if self.player.heads_or_tails != self.player.real_coin_value:
            self.player.player_is_lying = 1

class RoundResults(Page):
    def vars_for_template(self):
        template_vars = {"real_coin_value": self.player.real_coin_value,
                "guess": self.player.heads_or_tails,
                "accumulated_payoff": self.player.participant.vars["payoff_"+Constants.name_app],
                "last_round": self.round_number == Constants.num_rounds,
                "pay_random_app": self.session.config["pay_random_app"]}

               

        return template_vars


page_sequence = [Introduction, TossingTheCoin, Report, 
# FinalProcessing
RoundResults]
