from otree.api import Currency as c, currency_range,SubmissionMustFail
from . import views
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):
    p1=random.randint(0,Constants.endowment)

 
    p21=random.randint(0,Constants.multiplication_factor)
    p22=random.randint(0,Constants.multiplication_factor*2)
    p23=random.randint(0,Constants.multiplication_factor*3)
    p24=random.randint(0,Constants.multiplication_factor*4)
    p25=random.randint(0,Constants.multiplication_factor*5)
    p26=random.randint(0,Constants.multiplication_factor*6)
    p27=random.randint(0,Constants.multiplication_factor*7)
    p28=random.randint(0,Constants.multiplication_factor*8)
    p29=random.randint(0,Constants.multiplication_factor*9)
    p210=random.randint(0,Constants.multiplication_factor*10)

    def play_round(self):
        
        yield views.Introduction

        if self.player.id_in_group == 1:
            yield views.SendStrategyMethod, {"sent_amount_strategy" : self.p1}
        elif self.player.id_in_group == 2: 
            yield views.SendBackStrategyMethod, {"sent_back_amount_strategy_3":self.p21,
                                                "sent_back_amount_strategy_6":self.p22,
                                                "sent_back_amount_strategy_9":self.p23,
                                                "sent_back_amount_strategy_12":self.p24,
                                                "sent_back_amount_strategy_15":self.p25,
                                                "sent_back_amount_strategy_18":self.p26,
                                                "sent_back_amount_strategy_21":self.p27,
                                                "sent_back_amount_strategy_24":self.p28,
                                                "sent_back_amount_strategy_27":self.p29,
                                                "sent_back_amount_strategy_30":self.p210}
        
        #if self.player.id_in_group == 1:
        #    yield views.Send, {"sent_amount": 4}

        #else:
        #    yield views.SendBack, {'sent_back_amount': 8}

        yield views.Results

        #Corroborar pagos:
        if self.player.id_in_group == 1:
            if self.player.sent_amount_strategy == 0:
                assert self.player.payoff == Constants.endowment, "El pago no cuadra"
            elif self.player.sent_amount_strategy > 0:
                assert self.player.payoff== Constants.endowment - self.player.sent_amount_strategy + self.group.sent_back_amount, "El pago no cuadra"
            print(self.p1,self.player.payoff,self.player.sent_amount_strategy)
        elif self.player.id_in_group == 2:
            if self.group.sent_amount == 0:
                assert self.player.payoff == 0
            elif self.group.sent_amount == 1:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_3, "El pago no cuadra"
            elif self.group.sent_amount == 2:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_6, "El pago no cuadra"
            elif self.group.sent_amount == 3:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_9, "El pago no cuadra"
            elif self.group.sent_amount == 4:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_12, "El pago no cuadra"
            elif self.group.sent_amount == 5:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_15, "El pago no cuadra"
            elif self.group.sent_amount == 6:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_18, "El pago no cuadra"
            elif self.group.sent_amount == 7:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_21, "El pago no cuadra"
            elif self.group.sent_amount == 8:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_24, "El pago no cuadra"
            elif self.group.sent_amount == 9:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_27, "El pago no cuadra"
            elif self.group.sent_amount == 10:
                assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_30, "El pago no cuadra"

            print(self.player.payoff, self.player.sent_back_amount_strategy_3,
            self.player.sent_back_amount_strategy_6,
            self.player.sent_back_amount_strategy_9,
            self.player.sent_back_amount_strategy_12,
            self.player.sent_back_amount_strategy_15,
            self.player.sent_back_amount_strategy_18,
            self.player.sent_back_amount_strategy_21,
            self.player.sent_back_amount_strategy_24,
            self.player.sent_back_amount_strategy_27,
            self.player.sent_back_amount_strategy_30,
            'sent back amount is:', self.group.sent_back_amount)
        print(f'Todo salio bien para jugador {self.player.id_in_group}')
