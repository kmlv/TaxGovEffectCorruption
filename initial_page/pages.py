from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class InitialPage(Page):
    pass


page_sequence = [InitialPage]
