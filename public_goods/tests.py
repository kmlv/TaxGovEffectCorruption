from otree.api import (
    Currency as c, currency_range, SubmissionMustFail,expect
)
from . import views
from ._builtin import Bot
from .models import Constants
import random 


class PlayerBot(Bot):

    cases = ['basic', 'min', 'max']

    p1 = random.randint(1,Constants.endowment)
    p2 = random.randint(1,Constants.endowment)
    p3 = random.randint(1,Constants.endowment)
    p4 = random.randint(1,Constants.endowment)

    def play_round(self):
        
        yield views.Introduction

        # Verificando que valores extremos ni decimales funcionen

        for extreme_value in [-5.5,-100,-1,Constants.endowment+1,5.4]:

            yield SubmissionMustFail(views.Contribute, {
                'contribution':extreme_value
            })

        if self.player.id_in_group == 1:
            yield views.Contribute, {"contribution" : self.p1}
        elif self.player.id_in_group == 2: 
            yield views.Contribute, {"contribution":self.p2}
        elif self.player.id_in_group == 3: 
            yield views.Contribute, {"contribution":self.p3}
        else:
            yield views.Contribute, {"contribution":self.p4}

        # Corroborando que los pagos sean los correctos
        pago = (Constants.endowment - self.player.contribution) + self.group.individual_share
        
        yield views.Results

        print(self.player.round_payoff,pago)

        assert self.player.round_payoff == pago, "El pago no cuadra"

        print(f'Todo salio bien para jugador {self.player.id_in_group}')

        

        
    

        
            
