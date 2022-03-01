from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class Processing_payoff(Page):

    timeout_seconds = 1

    def before_next_page(self):
        self.player.set_final_payoffs()

class Payoffs(Page):
    def vars_for_template(self):

        apps = self.session.config["app_sequence"][1:-2]
        app_names = self.session.config["app_names"]

        payments = {app_names[app]:float(self.player.participant.vars['payoff_'+app]*self.session.config["exchange_rate"]) for app in apps}
        chosen_app_name = app_names[self.player.chosen_app]
        chosen_app_payment = self.player.participant.vars['payoff_'+self.player.chosen_app]

        chosen_app_payment_soles = chosen_app_payment * self.session.config["exchange_rate"]

        return dict(
            payments = payments,
            # chosen_app_payment = chosen_app_payment, # not in soles
            chosen_app_name = chosen_app_name,
            chosen_app_payment_plus_fee = float(chosen_app_payment_soles + self.session.config["participation_fee"]),
            chosen_app_payment_soles = float(chosen_app_payment_soles)
            #pay_random_app = self.session.config["pay_random_app"],
        )

class PaymentInfo(Page):

    def vars_for_template(self):
       
        return {
            'participant_id': self.player.participant.label,
        }

page_sequence = [Processing_payoff,Payoffs,PaymentInfo]
