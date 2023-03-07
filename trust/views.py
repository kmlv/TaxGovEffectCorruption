from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import config_leex_1

class Introduction(Page):
    #wait_for_all_groups = True

    def is_displayed(self):
        return self.round_number == 1

    def before_next_page(self):
        self.player.participant.vars["payoff_"+Constants.name_app] = 0


class Send(Page):
    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = models.Group
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.id_in_group == 1 and self.session.config["use_strategy_method"] is False

    def vars_for_template(self):
        amount = Constants.endowment

        return{
                'amount': amount }


class SendStrategyMethod(Page):
    """This page is for P1 and P2. They will both play both roles
    An hypothetic amount is sent by P1 and P2, and a response for 
    each possible scenario is chosen"""

    form_model = 'player'
    form_fields = ['sent_amount_strategy']

    def is_displayed(self):
        return self.session.config["use_strategy_method"] is True 


class SendBackStrategyMethod(Page):
    """This page is for P1 and P2. They will both play both roles
    An hypothetic amount is sent by P1 and P2, and a response for 
    each possible scenario is chosen"""

    form_model = 'player'
    form_fields = [f'sent_back_amount_strategy_{received}' 
                    for received in Constants.numbers]

    def is_displayed(self):
        return self.session.config["use_strategy_method"] is True 


class SendBackWaitPage(WaitPage):
    def is_displayed(self):
        return self.session.config["use_strategy_method"] is False


class SendBack(Page):
    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = models.Group
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.id_in_group == 2 and self.session.config["use_strategy_method"] is False

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplication_factor

        return {
                'tripled_amount': tripled_amount
        }

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplication_factor


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()
        if self.session.config["use_strategy_method"]:
            self.group.set_group_data()


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            # 'strategy_method': self.session.config["use_strategy_method"],
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor,
            'sent_back_amount': self.group.sent_back_amount,
            'last_round': Constants.num_rounds == self.round_number,
            'accumulated_payoff': self.player.participant.vars["payoff_"+Constants.name_app] + self.player.payoff
        }

    def before_next_page(self):

        # pass payoff to new var
        self.player.round_payoff = self.player.payoff
        self.player.participant.vars["payoff_"+Constants.name_app] += self.player.payoff
        print(f"self.player.participant.vars['payoff_'+Constants.app] = {self.player.participant.vars['payoff_'+Constants.name_app]}")
        
        # if config_leex_1.paid_game == Constants.name_app and config_leex_1.paid_round == self.round_number:
        #     self.player.payoff = self.player.payoff
        # else:
        #     self.player.payoff = 0


page_sequence = [
    Introduction,
    Send,
    SendStrategyMethod,
    SendBackStrategyMethod,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
