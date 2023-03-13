from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from . import config as config_py
import random, json


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


def assign_dictator(dictators_in_session: list, groups_with_dicts: list, group_matrix: list) -> list:
    """
    Assigns a dictator to each group that requires one
    """
    print("----Assign dictator----")

    index = 0
    if len(dictators_in_session) > 0:
        print("Dictators in session: ", dictators_in_session)
        print("Groups with dictators: ", groups_with_dicts)
        print("Group matrix: ", group_matrix)        
        for dictator in dictators_in_session:
            print("---")
            print("Current dictator: ", dictator)
            group_index = groups_with_dicts[index] - 1 # getting index of group with dictator
            current_group = group_matrix[group_index]
            print("Group index: ", group_index)
            print("Group matrix before update: ", group_matrix)
            print("Current group: ", group_matrix[group_index])
            current_group.append(dictator) # adding the benevolent dictator to the group
            print("Group matrix after update: ", group_matrix)
            index += 1

            if index == len(groups_with_dicts) or \
               index == len(dictators_in_session) : # break if more dictators than groups or no more dictators
                return group_matrix, dictators_in_session[index:] # return group and non assigned dictators
    else: # if no dictators in session
        return group_matrix, []


class Constants(BaseConstants):

    name_in_url = 'real_effort'

    # The total number of dictionaries in the data list in config.py is the
    # number of game rounds
    num_rounds = config_py.num_rounds
    num_groups = len(config_py.data_grps)

    dictators_file = open("dictators.json", "r")
    dictators = json.loads(dictators_file.read())

    players_per_group = 5 # 5 in prod
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
        "multiplicar el monto total reportado por",
        " y apropiarse de un ",
        "% del total."
    ]

    maxdistance1 = len(reference_texts[0])
    maxdistance2 = len(reference_texts[1])
    allowed_error_rates = [0, 0.99]
    contact_template = "real_effort2/Contactenos.html"

    
class Subsession(BaseSubsession):
    # Executed when the session is created
    def creating_session(self):
        # k is a scalar that will allow to randomize the audits

        for p in self.get_players():
            k = random.randint(1, 100)/100
            p.audit = k <= self.session.config["audit_prob"]
    

class Group(BaseGroup):
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
    task_earnings = models.CurrencyField()
    income_before_taxes = models.CurrencyField()
    income_after_taxes = models.CurrencyField()
    income_after_audit = models.CurrencyField()
    transcribed_text = models.LongStringField()
    levenshtein_distance = models.IntegerField()
    ratio = models.FloatField()
    contribution = models.CurrencyField(min = 0, initial = -1)
    endowment = models.CurrencyField()
    spanish = models.BooleanField()
    done = models.BooleanField()
    transcriptionDone = models.BooleanField()
    round_payoff = models.CurrencyField()
    chosen_round = models.IntegerField()
    income = models.CurrencyField()
    refText = models.LongStringField()
    audit = models.BooleanField()