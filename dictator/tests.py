from otree.api import Currency as c, currency_range, SubmissionMustFail, expect
from . import views
from ._builtin import Bot
from .models import Constants
import simplejson

class PlayerBot(Bot):
    def play_round(self):
        with open('dictator/test_cases.json','r',encoding='utf-8') as json_file:
            values=simplejson.load(json_file)
        valid_values=values['values_validation']

        yield views.Introduction

        #Valores fuera del rango [0,100], palabras o caracteres no deberían ser considerados:
        for value in valid_values['valid_kept']:
            yield SubmissionMustFail(views.Offer,{"kept":value})
        
        yield views.Offer, dict(kept= 55)

        yield views.Results

        #Corroborando pagos
        if self.player.dictator == True:
            assert self.player.payoff == self.group.group_kept, "el pago no es el correcto"
            
            print(f'Todo salio bien para jugador {self.player.id_in_group}')
        else:
            assert self.player.payoff == Constants.endowment - self.group.group_kept, "el pago no es el correcto"
            
            print(f'Todo salio bien para jugador {self.player.id_in_group}')

        print(self.player.payoff,self.group.group_kept,'Es dictator:',self.player.dictator==True)

        #if self.player.id_in_group == 1:
        #    yield (views.Offer, {"kept": c(99)})
        #    assert self.player.payoff == c(99)
        #else:
        #    assert self.player.payoff == c(1)

