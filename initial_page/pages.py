from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class E2lab_page(Page):
    pass

class InitialPage(Page):
    pass


page_sequence = [E2lab_page,InitialPage]
