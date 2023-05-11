from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random, json

import config_leex_1

doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>. The differences between using strategy method or not can be found <a href="https://citeseerx.ist.psu.edu/view
doc/download?doi=10.1.1.597.7870&rep=rep1&type=pdf" target="_blank"> here</a>
"""


class Constants(BaseConstants):
    name_in_url = 'app_das'
    name_app='trust'
    players_per_group = 2
    num_rounds = 2

    contact_template = "trust/Contactenos.html"
    instructions_template = 'trust/Instructions.html'

    # Initial amount allocated to each player
    endowment = 33
    multiplication_factor = 3

    # Strategy method
    choice_step = 3 
    choices_trustor = [choice for choice in range(0, endowment+1, choice_step)]
    print(choices_trustor)
    #create labels from constants and multiplier:
    number=[]
    for value in range(multiplication_factor,endowment*multiplication_factor+1,multiplication_factor):
        number.append(str(value))
    labe = ['sent_back_amount_strategy_' + value for value in number]
    label=[]
    numbers=[]
    choices_possible=[]
    x=0
    for value in labe:
        x=x+1
        if x % 3 == 0:
            label.append(value)
            x1=x*multiplication_factor
            numbers.append(x1)
            choices_possible.append(x)
        else:
            pass
    print(number)
    print(numbers)
    print(label)
    print(choices_possible)

    #list with numbers from 1 to endowment:
    list_c=[number for number in numbers]


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly(fixed_id_in_group=True)

    def vars_for_admin_report(self):
        # amount sent in average
        amounts_sent = [p.sent_amount_strategy for p in self.get_players() if p.sent_amount_strategy != None]
        avg_sent = "no data"
        if len(amounts_sent) != 0:
            avg_sent = sum(amounts_sent)/len(amounts_sent)

        # amount sent back in average per case
        amounts_sent_back = {}
        for labe, numb in zip(Constants.label,Constants.numbers):
            numb='received_'+numb
            labe='p.'+labe
            amounts_sent_back[numb] = [labe for p in self.get_players() if labe != None]
       
        # telling if there are values for all sent back amounts
        there_are_sent_backs = False
        aux_counter = 0 # for counting how many values from amounts_sent_back are not empty
        for choice in Constants.numbers:
            if amounts_sent_back[f"received_{choice}"]:
                amounts_sent_back[f"received_{choice}"] = sum(amounts_sent_back[f"received_{choice}"])/len(amounts_sent_back[f"received_{choice}"])
                aux_counter += 1
        
        if aux_counter == len(Constants.choices_trustor) - 1: # True if all values aren't empty (omitting 0)
            there_are_sent_backs = True

        if amounts_sent and there_are_sent_backs:
            return {**{'avg_sent': avg_sent}, **amounts_sent_back}

        else:   
            sent_backs_no_data = {}
            for choice in Constants.number:
                sent_backs_no_data[f"received_{choice}"] = '(no data)'
            return {**{'avg_sent': '(no data)'}, **sent_backs_no_data}


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""Amount sent by P1""",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""",
        min=c(0),
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if self.session.config["use_strategy_method"] is False:
            if self.round_number == 1:
                p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
                p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount
            else:
                p2.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
                p1.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount
       
        else:
            if self.round_number == 1:
                if p1.sent_amount_strategy == 0:
                    p1.payoff = Constants.endowment
                    p2.payoff = 0
                    self.sent_back_amount = 0
                else:
                    for value, label in zip(Constants.choices_possible, Constants.label) :
                        if p1.sent_amount_strategy == value:
                            p1.payoff = Constants.endowment - p1.sent_amount_strategy + getattr(p2,label)
                            p2.payoff = p1.sent_amount_strategy * Constants.multiplication_factor - getattr(p2,label)
                            self.sent_back_amount = getattr(p2,label)
            else:
                if p2.sent_amount_strategy == 0:
                    p2.payoff = Constants.endowment
                    p1.payoff = 0
                    self.sent_back_amount = 0
                else:
                    for value, label in zip(Constants.choices_possible, Constants.label) :
                        if p2.sent_amount_strategy == value:
                            p2.payoff = Constants.endowment - p2.sent_amount_strategy + getattr(p1,label)
                            p1.payoff = p2.sent_amount_strategy * Constants.multiplication_factor - getattr(p1,label)
                            self.sent_back_amount = getattr(p1,label)
                        
    def set_group_data(self):
        for p in self.get_players():
            if p.role() == 'A':
                self.sent_amount = p.sent_amount_strategy
    

# function for strategy method fields (trustee)
def make_sent_back_field(received_amount):
    return models.IntegerField(
    choices=[choice for choice in range(received_amount + 1)],
    label=f"Si recibieras {received_amount} puntos, ¿cuánto enviarías de vuelta al Jugador A?"
)

class Player(BasePlayer):

    round_payoff = models.CurrencyField()

    # strategy method fields
    ## for trustor
    trustor = models.BooleanField(initial=False)
    sent_amount_strategy = models.CurrencyField(
            min=0, max=Constants.endowment,
            choices=Constants.choices_trustor,
            verbose_name="""¿Cuánto enviarías al Jugador B?""",
        )

    ## for trustee
    trustee = models.BooleanField(initial=False)

    for labe, numb in zip(Constants.label,Constants.numbers):
        locals()[labe]=models.IntegerField(
                            choices=[choice for choice in range(0,int(numb) + 1,3)],
                            label=f"Si recibieras {numb} puntos, ¿cuánto enviarías de vuelta al Jugador A?")
    del labe
    del numb


    def role(self):
        if self.round_number == 1:
            return {1: 'A', 2: 'B'}[self.id_in_group]
        else:
            return {1: 'B', 2: 'A'}[self.id_in_group]
