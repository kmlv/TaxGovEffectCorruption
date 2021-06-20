from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from . import config as config_py
import random


doc = """
This is a game that combines elements of the Public Goods game and real-effort
transcription task into one. This game has 2 modes, one with transcription off and one 
with transcription on. In mode 1, where transcription mode is off, each player has a 
fixed income and must determine how much of his/her income to report. A tax of X% is
automatically collected from each player's reported income. The total tax collected is 
multiplied by a specified multiplier and then divided evenly among all players in the 
group. Each player's total money is the amount of income remaining after tax is deducted 
from their income plus his/her share of the total tax money.

In mode 2, Subjects are shown two images of incomprehensible text.
Subjects are required to transcribe (copy) the text into a text entry field.
The quality of a subject's transcription is measured by the
<a href="http://en.wikipedia.org/wiki/Levenshtein_distance">Levenshtein distance</a>.
The accuracy of the players' transcription of the second image ultimately determines
each person's initial income. The remainder of mode 2 follows mode 1.
"""


def levenshtein(a, b):
    """Calculates the Levenshtein distance between a and b."""
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current = range(n + 1)

    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]

            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def distance_and_ok(transcribed_text, reference_text, max_error_rate):
    error_threshold = len(reference_text) * max_error_rate
    distance = levenshtein(transcribed_text, reference_text)
    ok = distance <= error_threshold
    return distance, ok


class Constants(BaseConstants):

    name_in_url = 'real_effort'

    # The total number of dictionaries in the data list in config.py is the
    # number of game rounds
    num_rounds = config_py.num_rounds
    num_groups = len(config_py.data_grps)
    players_per_group = 3 # 5 in prod
    instructions_template = 'real_effort2/Instructions.html'
    info_code = 'real_effort/Code.html'

    # List of the incomprehensible text that the players must transcribe
    reference_texts = [
        "Revealed preference",
        "Hex ton satoha egavecen. Loh ta receso minenes da linoyiy xese coreliet ocotine! Senuh asud tu bubo "
        "tixorut sola, bo ipacape le rorisin lesiku etutale saseriec niyacin ponim na. Ri arariye senayi esoced "
        "behin? Tefid oveve duk mosar rototo buc: Leseri binin nolelar sise etolegus ibosa farare. Desac eno "
        "titeda res vab no mes!",
    ]

    # Text of decisions that the authority can make
    decisions = [
        "no modificar el dinero obtenido por impuestos.",
        " multiplicar el monto total reportado por",
        " y apropiarse de un ",
        "% del total."
    ]

    maxdistance1 = len(reference_texts[0])
    maxdistance2 = len(reference_texts[1])
    allowed_error_rates = [0, 0.99]

    
class Subsession(BaseSubsession):
    # Executed when the session is created
    def creating_session(self):
        # k is a scalar that will allow to randomize the audits
        k = random.randint(0, 1)
        round_number = self.round_number

        for p in self.get_players():
            p.audit2 = k

        # getting player groups
        total_amount_of_players = len(self.get_players())
        
        # setting new group matrix
        if round_number == 1:
            group_matrix = config_py.grouping_algorithm(total_amount_of_players, Constants.players_per_group)
            self.set_group_matrix(group_matrix)
        else:
            self.group_like_round(round_number - 1) # grouping like round 1

        # TODO: set parameters for group variables
        for grp in self.get_groups():
            
            # getting the id of each group
            group_id = str(grp.id_in_subsession % Constants.players_per_group)
            if group_id != 0:
                group_key = "group_" + str(group_id)
            else:
                group_key = "group_4"

            # obtaining the group parameters
            group_parameters = config_py.data_grps[group_key]
            if self.round_number <= round(Constants.num_rounds/2):
                round_parameters = group_parameters["first_half"] # parameters for first half of rounds
            else:
                round_parameters = group_parameters["second_half"] # parameters for second half of rounds
            
            # TODO: set parameters for every group
            grp.multiplier = round_parameters["multiplier"]
            grp.authority = round_parameters["authority"]
            grp.appropriation_percent = round_parameters["appropriation_percent"]
            grp.tax_percent = round_parameters["tax"]
            grp.penalty_percent = round_parameters["penalty"]
            grp.transcription_required = round_parameters["transcription"]
            grp.transcription_difficulty = round_parameters["difficulty"]
            grp.spanish = round_parameters["spanish"]
            
        # Initialization of default ratio, contribution, and income values for each player
        for p in self.get_players():
            p.ratio = 1
            p.contribution = 0
            p.endowment = round_parameters["end"]


class Group(BaseGroup):
    baseIncome = models.CurrencyField()
    total_report = models.CurrencyField()
    total_contribution = models.CurrencyField()
    total_earnings = models.CurrencyField()
    individual_share = models.CurrencyField()
    temp = models.IntegerField()

    # ID of randomly-chosen authority player
    authority_ID = models.IntegerField()

    # Does the authority decide to multiply the reported income by the multiplier?
    # This applies to both mode 1 and mode 2 choice 1
    authority_multiply = models.BooleanField()

    # Does the authority decide on mode 2 choice (appropriate a percentage of the money for
    # him/herself)?
    auth_appropriate = models.BooleanField()
    total_reported_income = models.CurrencyField()
    appropriation = models.CurrencyField()

    # main parameters
    multiplier = models.FloatField() # public goods multiplier
    authority = models.StringField() # type of authority
    appropriation_percent = models.FloatField() # percentage the authority can/will appropiate
    tax_percent = models.FloatField() # income percentage that goes for taxes
    penalty_percent = models.FloatField() # income percentage that goes as penalty for bad audit
    transcription_required = models.BooleanField() # True if required, else False
    treatment_tag = models.StringField() # tag of current treatment
    spanish = models.BooleanField() # True if spanish, else False
    transcription_difficulty = models.IntegerField()


class Player(BasePlayer):
    audit2 = models.IntegerField()
    income_before_taxes = models.CurrencyField()
    transcribed_text = models.LongStringField()
    transcribed_text2 = models.LongStringField()
    levenshtein_distance = models.IntegerField()
    ratio = models.FloatField()
    contribution = models.CurrencyField(min = 0, initial = -1)
    endowment = models.CurrencyField()
    spanish = models.BooleanField()
    done = models.BooleanField()
    transcriptionDone = models.BooleanField()
    # payoff = models.CurrencyField()
    income = models.CurrencyField(initial=0)
    refText = models.LongStringField()
    audit = models.BooleanField()