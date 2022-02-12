from otree.api import Currency as c, currency_range,SubmissionMustFail
from . import views
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):


    def play_round(self):
        
        p1=random.randint(0,Constants.endowment)
        #create random numbers that depends on the endowment
        list_players=[]
        for value in range(1,Constants.endowment+1):
            list_players.append("p2"+str(value))

        list_numbers=[number for number in range(1,Constants.endowment+1)]
        list_p=[]

        for labe, numb in zip(list_players, list_numbers):
            locals()[labe]=random.randint(0,Constants.multiplication_factor*int(numb))
            list_p.append(locals()[labe])
        del labe   

        yield views.Introduction   
        
        if self.player.id_in_group == 1:
            yield views.SendStrategyMethod, {"sent_amount_strategy" : p1}
        elif self.player.id_in_group == 2: 
            yield views.SendBackStrategyMethod, dict(zip(Constants.label, list_p)) 

        
        #if self.player.id_in_group == 1:
        #    yield views.Send, {"sent_amount": 4}

        #else:
        #    yield views.SendBack, {'sent_back_amount': 8}

        yield views.Results

        #Corroborar pagos:
        if self.player.id_in_group == 1:
            if self.player.sent_amount_strategy == 0:
                assert self.player.payoff == Constants.endowment, "Player 1: El pago no cuadra"
            elif self.player.sent_amount_strategy > 0:
                assert self.player.payoff== Constants.endowment - self.player.sent_amount_strategy + self.group.sent_back_amount, "Player 1: El pago no cuadra"
            print(p1,self.player.payoff,self.player.sent_amount_strategy)
        
        elif self.player.id_in_group == 2:
            for value, label in zip(Constants.list_c,Constants.label):
                if self.group.sent_amount == 0:
                    assert self.player.payoff == 0
                elif self.group.sent_amount == value:
                    assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - getattr(self.player,label), "Player 2: El pago no cuadra"
        #     if self.group.sent_amount == 0:
        #         assert self.player.payoff == 0
        #     elif self.group.sent_amount == 1:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_3, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 2:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_6, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 3:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_9, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 4:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_12, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 5:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_15, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 6:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_18, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 7:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_21, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 8:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_24, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 9:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_27, "Player 2: El pago no cuadra"
        #     elif self.group.sent_amount == 10:
        #         assert self.player.payoff == self.group.sent_amount * Constants.multiplication_factor - self.player.sent_back_amount_strategy_30, "Player 2: El pago no cuadra"

            print(self.player.payoff, 'sent back amount is:', self.group.sent_back_amount)
        print(f'Todo salio bien para jugador {self.player.id_in_group}')
