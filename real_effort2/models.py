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
    index = 0
    if len(dictators_in_session) > 0:
        for dictator in dictators_in_session:
            group_index = groups_with_dicts[index] - 1 # getting index of group with dictator
            group_matrix[group_index].append(dictator) # adding the benevolent dictator to the group
            index += 1

            if index == len(groups_with_dicts) or \
               index == len(dictators_in_session) : # break if more dictators than groups or no more dictators
                return (group_matrix, dictators_in_session[index:]) # return group and non assigned dictators
    else: # if no dictators in session
        return (group_matrix, [])


class Constants(BaseConstants):

    name_in_url = 'real_effort'

    # The total number of dictionaries in the data list in config.py is the
    # number of game rounds
    num_rounds = config_py.num_rounds
    num_groups = len(config_py.data_grps)

    dictators_file = open("dictators.json", "r")
    dictators = json.loads(dictators_file.read())

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
        round_number = self.round_number

        for p in self.get_players():
            k = random.randint(1, 100)/100
            p.audit = k <= self.session.config["audit_prob"]

        group_matrix = [[] for group in range(Constants.num_groups)]

        # reading dictators
        benevolent_dictators = Constants.dictators["benevolent"]
        embezzlement_dictators = Constants.dictators["embezzlement"]

        # getting num of required dictators
        num_req_benevolents = config_py.num_groups_with_dictators*config_py.num_benevolents_per_group
        num_req_embezzlements = config_py.num_groups_with_dictators*config_py.num_embezzlements_per_group
        
        # getting group ids of groups with dictators
        groups_with_dicts = []
        for group in config_py.data_grps.keys():
            if config_py.data_grps[group]["first_half"]["authority"] != "no authority" \
                or config_py.data_grps[group]["second_half"]["authority"] != "no authority":
                groups_with_dicts.append(int(group[-1]))

        # setting new group matrix
        print(f"round_num = {round_number}")
        if round_number == 1:
            # getting players by type
            benevolents_in_session = [player.id_in_subsession for player in self.get_players() if player.label in benevolent_dictators]
            embezzlements_in_session = [player.id_in_subsession for player in self.get_players() if player.label in embezzlement_dictators]
            non_dictators = [player.id_in_subsession for player in self.get_players() if player.id_in_subsession not in benevolents_in_session and player.id_in_subsession not in embezzlements_in_session]
            
            # shuffling players order
            random.shuffle(benevolents_in_session)
            random.shuffle(embezzlements_in_session)
            random.shuffle(non_dictators)
            
            # assigning dictators to grous
            updated_groups, non_assigned_benev = assign_dictator(benevolents_in_session, groups_with_dicts, group_matrix)
            updated_groups, non_assigned_embez = assign_dictator(embezzlements_in_session, groups_with_dicts, updated_groups)

            # completing groups with non dictators
            unassigned_players = non_dictators + non_assigned_benev + non_assigned_embez
            initial_index = 0 # first index for slicing non dictators
            for group_list in updated_groups:
                num_unassigned = Constants.players_per_group - len(group_list) # num of required participants to complete group
                final_index = initial_index + num_unassigned # final index for slicing non dictators                
                group_list += unassigned_players[initial_index:final_index] # assigning non dictators to group
                initial_index = num_unassigned
            
            self.set_group_matrix(updated_groups) # setting groups after assignment

        else:
            self.group_like_round(1) # grouping like round 1
        
        for grp in self.get_groups(): # setting group parameters
            
            # obtaining the group parameters
            group_parameters = config_py.data_grps[f"group_{grp.id_in_subsession}"]
            
            if self.round_number <= round(Constants.num_rounds/2):
                round_parameters = group_parameters["first_half"] # parameters for first half of rounds
            else:
                round_parameters = group_parameters["second_half"] # parameters for second half of rounds
            
            grp.multiplier = round_parameters["multiplier"]
            grp.authority = round_parameters["authority"]
            grp.appropriation_percent = round_parameters["appropriation_percent"]
            grp.tax_percent = round_parameters["tax"]
            grp.penalty_percent = round_parameters["penalty"]
            grp.transcription_required = round_parameters["transcription"]
            grp.transcription_difficulty = round_parameters["difficulty"]
            grp.treatment_tag = round_parameters["tag"]
            grp.spanish = round_parameters["spanish"]

        # Initialization of default ratio, contribution, and income values for each player
        for p in self.get_players():
            p.ratio = 1
            p.contribution = 0
            p.endowment = round_parameters["end"]
    

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
    total_reported_income = models.CurrencyField()
    appropriation = models.CurrencyField(initial=0)

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
    transcribed_text2 = models.LongStringField()
    levenshtein_distance = models.IntegerField()
    ratio = models.FloatField()
    contribution = models.CurrencyField(min = 0, initial = -1)
    endowment = models.CurrencyField()
    spanish = models.BooleanField()
    done = models.BooleanField()
    transcriptionDone = models.BooleanField()
    # payoff = models.CurrencyField()
    income = models.CurrencyField()
    refText = models.LongStringField()
    audit = models.BooleanField()