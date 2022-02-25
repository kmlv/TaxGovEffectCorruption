from otree.api import Currency as c, currency_range, Submission
from . import views
from ._builtin import Bot
from .models import Constants

class PlayerBot(Bot):

    def play_round(self):
        
        yield Submission(views.Processing_payoff, check_html = False, timeout_happened=True)
        yield views.Payoffs 
        yield views.PaymentInfo
