from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class E2lab_page(Page):
    pass

class InitialPage(Page):
    def vars_for_template(self):
        participation_fee=self.session.config['participation_fee']
        ratio=self.session.config['real_world_currency_per_point']
        ratio=round(1/ratio,2)
        currency=self.session.config['custom_name']
        return dict(
            participation_fee=participation_fee,
            ratio=ratio,
            currency=currency,
        )


page_sequence = [E2lab_page,InitialPage]
