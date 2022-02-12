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

        yield pages.RoundResults

        # Chequeando si el pago final es igual a Nro de caras X 10

        if self.player.round_number == Constants.num_rounds:
            
            acumulado = 0
            for player in self.player.in_all_rounds():
                acumulado += player.payoff 

            print(f'Suma de pagos {acumulado}', f'Nro de Caras por 10 {10*self.R}')

            assert acumulado == 10*self.R, "No cuadra el payoff final"

            print('Si cuadro los pagos')

