from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Final_E2lab(Page):
    def vars_for_template(self):
        return dict(participant_id=self.participant.label)




page_sequence = [Final_E2lab]
