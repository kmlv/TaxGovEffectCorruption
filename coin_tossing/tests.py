from otree.api import Currency as c, currency_range, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    R = random.randint(1,Constants.num_rounds)

    cara = ["Cara"]*R
    sello = ["Sello"]*(Constants.num_rounds-R)

    # Lista que contiene las decisiones que tomara el BOT en cada una de las rondas

    lista = cara + sello

    random.shuffle(lista)

    print(lista)

    def play_round(self):

        if self.player.round_number == 1:

            yield pages.Introduction

        yield Submission(pages.TossingTheCoin, check_html = False, timeout_happened=True)

        # Realizando las decisiones por ronda

        for round, decision in zip(range(1,Constants.num_rounds+1),self.lista):
            
            if self.player.round_number == round:
                
                yield pages.Report, {'heads_or_tails':decision}

                print(f'El valor real: {self.player.real_coin_value}',f'El valor escogido: {decision}')
                print(f'El pago de la ronda {round}: {self.player.payoff}')
            
                assert self.player.real_coin_value != None, "No se esta guardando el toss"

        # Chequeando si el pago final es igual a Nro de caras X 10

        #if self.player.round_number == Constants.num_rounds: 
        #    yield Submission(pages.FinalProcessing, check_html = False, timeout_happened=True)
        
        yield pages.RoundResults
        
        if self.player.round_number == Constants.num_rounds: #and self.session.config["pay_random_app"]
            
            acumulado = 0
            for player in self.player.in_all_rounds():
                acumulado += player.payoff 

            print(f'Suma de pagos {acumulado}', f'Nro de Caras x 10 = {Constants.head_payment*self.R}')

            assert acumulado == Constants.head_payment*self.R, "No cuadra el payoff final"

            print('Si cuadro los pagos')

            # Verificando si el pago final del participante es igual al pago de la app elegida

            #app_pago = self.player.chosen_app

            #print('La app para el pago final es: ',app_pago)

            #assert self.participant.vars["payoff_"+app_pago] == self.participant.payoff, 'Los pagos no coinciden'

            #print('El pago de la app '+app_pago+' coincide con el pago final del participante')


        

