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
    config = config_py.export_data()
    name_in_url = 'real_effort'

    # The total number of dictionaries in the data list in config.py is the
    # number of game rounds
    num_rounds = len(config[0])
    players_per_group = 2
    instructions_template = 'real_effort2/Instructions.html'
    info_code = 'real_effort/Code.html'

    # List of the incomprehensible text that the players must transcribe
    reference_texts = [
        "Revealed preference",
        "Hex ton satoha egavecen. Loh ta receso minenes da linoyiy xese coreliet ocotine! Senuh asud tu bubo tixorut sola, bo ipacape le rorisin lesiku etutale saseriec niyacin ponim na. Ri arariye senayi esoced behin? Tefid oveve duk mosar rototo buc: Leseri binin nolelar sise etolegus ibosa farare. Desac eno titeda res vab no mes!",
    ]

    # Text of decisions that the authority can make
    decisions = [
        "not modify the taxed income multiplier.",
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
        # Shuffle players randomly so that they can end up in any group
        # k is a scalar that will allow to randomize the audits
        k = random.randint(0, 1)
        config = Constants.config
        round_number = self.round_number
        shuffle = config[0][round_number - 1]["shuffle"]
        for p in self.get_players():
            p.audit2 = k

        print("Round number: ", round_number, ", Shuffle: ", shuffle)

        # After round 1, decision to shuffle the groups is based on whether the value for the "shuffle" key for the
        # current round's dictionary entry is True
        if round_number == 1:
            self.group_randomly()

        else:
            if shuffle == True:
                self.group_randomly(fixed_id_in_group=True)
            else: # Keep the groups organized the same as in the previous round
                self.group_like_round(round_number - 1)

        print(self.get_group_matrix())
        print("---------------------------------------------------")

        # Initialization of default ratio, contribution, and income values for each player
        for p in self.get_players():
            p.ratio = 1
            p.contribution = 0
            p.spanish = Constants.config[0][round_number - 1]["spanish"]
            p.income = Constants.config[0][round_number - 1]["end"]


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


class Player(BasePlayer):
    audit2 = models.IntegerField()
    transcribed_text = models.LongStringField()
    transcribed_text2 = models.LongStringField()
    levenshtein_distance = models.IntegerField()
    ratio = models.FloatField()
    contribution = models.CurrencyField(min = 0, initial = -1)
    income = models.CurrencyField()
    spanish = models.BooleanField()
    done = models.BooleanField()
    transcriptionDone = models.BooleanField()
    payoff = models.CurrencyField()
    refText = models.LongStringField()
    audit = models.BooleanField()