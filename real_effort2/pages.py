from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, assign_dictator, distance_and_ok
from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import math
from random import *
import random
import string
from .config import data_grps


def writeText(text, fileName):
    """"This method generates the image with the garbled/randomized transcription text on it
    and saves it to fileName"""

    image = Image.open('real_effort2/background.png')
    image = image.resize((650, 100))
    image.save('real_effort2/background.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('real_effort2/Roboto-Regular.ttf', size=19)
    imageChars = 100
    numLines = len(text) / imageChars
    numLines = math.ceil(numLines)
    lines = []

    for i in range(numLines):
        if(imageChars * (i + 1) < len(text)):
            lines.append(text[imageChars * i : imageChars * (i+1)])
        else:
            lines.append(text[imageChars * i : len(text)])

    for i in range(numLines):
        (x, y) = (10, 20 * i)
        message = lines[i]
        print("Message is: ", message)
        color = 'rgb(0, 0, 0)' # black color
        draw.text((x, y), message, fill=color, font=font)

    image.save(fileName)


def generateText(difficulty):
    """This method generates randomized garbled text whose difficulty to transcribe is based on the difficulty paramaeter
    (between 1 to 3) that's passed in."""

    min_char = 4 * difficulty
    max_char = min_char + 6
    allchar = string.ascii_lowercase + string.digits + string.punctuation.replace(",", "").replace(";", "")
    vowels = ('a', 'e', 'i', 'o', 'u')

    #generated = "$abgfnu% hgancnya @mk.o)qwbn[apzxc[*}-en45a.m_nbczpi45&|jsn-omn^"
    generated=""

    if (difficulty == 1):
        allchar = string.ascii_lowercase
    if (difficulty == 2):
        allchar = string.ascii_lowercase + string.digits
    for i in range(10):
        for i in range(5):
            allchar += vowels[i]

    while (len(generated) < 70 - max_char):
        add = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
        generated += (add + ".")

    return generated


def getPageCode(self):
    """This method generates a page code in the format T_1_A_5, where the number after "T" represents the transcription
    mode (0 or 1) and the number after "A" represents the authority mode (1 or 2). This page code is displayed at the
    top right of every page in the game."""

    config = self.session.vars["config"]
    t_code = 0
    auth_code = config[0][self.round_number - 1]["mode"]

    if config[0][self.round_number - 1]["transcription"] == True:
        t_code = 1

    return "T" + str(t_code) + "_" + "A" + str(auth_code)


class InitialWaitPage(WaitPage):
    wait_for_all_groups = True    
    def after_all_players_arrive(self):
        # setting up groups (for first round)
        round_number = self.round_number
        group_matrix = [[] for _ in range(int(len(self.subsession.get_players())/Constants.players_per_group))]
        print("Number of groups", int(len(self.subsession.get_players())/Constants.players_per_group))
        print("group matrix: ", group_matrix)

        # reading dictators
        benevolent_dictators = Constants.dictators["benevolent"]
        embezzlement_dictators = Constants.dictators["embezzlement"]
        
        # getting group ids of groups with dictators
        groups_with_dicts = []
        for group in data_grps.keys():
            if data_grps[group]["first_half"]["authority"] != "no authority" \
                or data_grps[group]["second_half"]["authority"] != "no authority":
                groups_with_dicts.append(int(group[-1]))

        # setting new group matrix
        print(f"round_num = {round_number}")
        if round_number == 1:
            # getting players by type
            print("All players: ", self.subsession.get_players())
            benevolents_in_session = [player.id_in_subsession for player in self.subsession.get_players() if player.participant.label in benevolent_dictators]
            embezzlements_in_session = [player.id_in_subsession for player in self.subsession.get_players() if player.participant.label in embezzlement_dictators]
            non_dictators = [player.id_in_subsession for player in self.subsession.get_players() if player.id_in_subsession not in benevolents_in_session and player.id_in_subsession not in embezzlements_in_session]
            
            # shuffling players order
            random.shuffle(benevolents_in_session)
            random.shuffle(embezzlements_in_session)
            random.shuffle(non_dictators)
            print(f"Benevolent dictators: {benevolents_in_session}")
            print(f"Embezzlement dictators: {embezzlements_in_session}")
            print(f"Non dictators: {non_dictators}")

            # assigning dictators to grous
            updated_groups, non_assigned_benev = assign_dictator(benevolents_in_session, groups_with_dicts, group_matrix)
            print(f"Updated groups: {updated_groups}. Non assigned benevolent dicts: {non_assigned_benev}")
            updated_groups, non_assigned_embez = assign_dictator(embezzlements_in_session, groups_with_dicts, updated_groups)
            print(f"Updated groups: {updated_groups}. Non assigned embezzlement dicts: {non_assigned_embez}")

            # completing groups with non dictators
            unassigned_players = non_dictators + non_assigned_benev + non_assigned_embez
            print(f"Unassigned players: {unassigned_players}")
            initial_index = 0 # first index for slicing non dictators
            print("---Completting groups---")
            for group_list in updated_groups:
                print("--Current group list: ", group_list)
                num_unassigned = Constants.players_per_group - len(group_list) # num of required participants to complete group
                print("Current num_unassigned: ", num_unassigned)
                final_index = initial_index + num_unassigned # final index for slicing non dictators                
                print("Current indexes: ", (initial_index, final_index))
                group_list += unassigned_players[initial_index:final_index] # assigning non dictators to group
                print("Current group_list: ", group_list)
                initial_index = final_index
                print("Next initial_index: ", initial_index)
                            
            print(f"Final groups: {updated_groups}")
            self.subsession.set_group_matrix(updated_groups) # setting groups after assignment

    def is_displayed(self):
        if self.round_number == 1:
            return True
        else:
            self.subsession.group_like_round(1) # grouping like round 1
            return False


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    
    def is_displayed(self):
        # setting group parameters
        if self.group.treatment_tag is None: # if parameters haven't been updated yet (default contr = -1)
            for grp in self.subsession.get_groups(): 
                # obtaining the group parameters
                group_parameters = data_grps[f"group_{grp.id_in_subsession}"]
                
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
                for p in grp.get_players():
                    p.ratio = 1
                    p.contribution = 0
                    p.endowment = round_parameters["end"]
                    if p.participant.label in Constants.dictators["benevolent"] and grp.authority == "benevolent":
                        grp.authority_ID = p.id_in_group
                    elif p.participant.label in Constants.dictators["embezzlement"] and grp.authority == "embezzlement":
                        grp.authority_ID = p.id_in_group
                    elif grp.authority == "no authority" and grp.authority_ID is None:
                        grp.authority_ID = random.randint(1, Constants.players_per_group)
                
                if grp.authority_ID is None:
                    grp.authority_ID = random.randint(1, Constants.players_per_group)

        # displaying page
        if (self.round_number == 1):
            return True
        else:
            return False

    
class InstructionsB(Page):
    """Description of the game block"""
    
    def vars_for_template(self):
        audit_prob = self.session.config["audit_prob"]
        display_tax_perc = str(round(self.group.tax_percent*100))+"%"
        display_audit_prob = str(round(audit_prob*100))+"%"
        display_penalty_perc = str(round(self.group.penalty_percent*100))+"%"   
        return {"appropiation_percent_display": str(round(self.group.appropriation_percent/2, 2)*100)+"%",
                "display_tax_perc": display_tax_perc,
                "audit_prob": display_audit_prob,
                "penalty": display_penalty_perc,
                "mult": round(self.group.multiplier)}  


class Transcribe(Page):
    """Transcription task that's shown to the player that determines the ratio sfor the player's starting income"""
    form_model = 'player'
    form_fields = ['transcribed_text']

    # la transcripcion se aproxima al entero mas cercano si la parte decimal es mayor a .5 (no mayor igual)
    def is_displayed(self):
        print("Inside Transcribe page")
        print("Transcription for this round is: " + str(self.group.transcription_required))

        if self.group.transcription_required == False:
            return False
        else:
            return True

    def vars_for_template(self):
        # creating an image with the text to be transcribed
        self.player.refText = generateText(self.group.transcription_difficulty)     
        return {
            # 'image_path': 'real_effort2/paragraphs/{}.png'.format(2),
            'reference_text': self.player.refText,
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rates[1]),
            'round_num': self.round_number
        }

    def transcribed_text_error_message(self, transcribed_text):
        """Determines the player's transcription accuracy."""

        reference_text = self.player.refText
        allowed_error_rate = Constants.allowed_error_rates[1] # allows .99 error rate
        distance, ok = distance_and_ok(transcribed_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance = distance
            self.player.ratio = 1 - distance / Constants.maxdistance2
        else:
            if allowed_error_rate == 0:
                return "La transcripción debe ser exactamente igual a la original."
            else:
                return "Para avanzar, debes transcribir más caracteres similares a la transcripción original."

    def before_next_page(self):
        # If transcription mode is set to true for this round, set the player's income according
        # to their transcription accuracy
        self.player.ratio = 1 - self.player.levenshtein_distance / len(self.player.refText)
        self.player.task_earnings = self.player.endowment * self.player.ratio
        self.player.income_before_taxes = self.player.task_earnings # assigning income bef taxes
        self.player.payoff = 0
        self.player.transcriptionDone = True


class ReportIncome(Page):
    """Page where the player reports his/her income"""
    form_model = 'player'
    form_fields = ['contribution']

    def contribution_max(self):
        """Dynamically sets the maximum amount of each player's income that he/she can report"""
        return self.player.income_before_taxes

    def vars_for_template(self):
        return {'tax': self.group.tax_percent * 100,
                'mult': self.group.multiplier,
                'display_ratio': round(self.player.ratio * 100, 1), 
                'endowment': self.player.endowment,
                'display_income': self.player.task_earnings, 
                'transcribe_on': self.group.transcription_required,
                'round_num': self.round_number
        }

    def before_next_page(self):
        self.player.income_after_taxes = self.player.income_before_taxes - self.player.contribution*self.group.tax_percent


class Audit(Page):
    """Alerts a player (if he/she has been chosen) that they have been audited and informs them whether their actual
    and reported income match. If not, they incur a penalty that's deducted from their remaining income after taxes
    are deducted."""
    def is_displayed(self):
       if self.player.audit == 1:
           return True
       else:
           return False

    def vars_for_template(self):
        player = self.player

        # If player's reported income and actual income don't match
        if player.contribution != player.income_before_taxes:
            player.income_after_audit = (1 - self.group.penalty_percent)*player.income_after_taxes
            
            return {
                'fail': True,
                'correctIncome': player.income_before_taxes,
                'reportedIncome': player.contribution,
                'newIncome': c(round(player.income_after_audit, 1)),
                'penalty': self.group.penalty_percent * 100,
                'round_num': self.round_number
            }
        else:
            player.income_after_audit = player.income_after_taxes
            return {
                'fail': False, 'round_num': self.round_number
            }


class NoAuthority(Page):
    """
    This page is displayed when there is no authority. A person will be selected
    randomly chosen to multiply the money. If he/she has also be selected to
    randomly receive 0.5, it will also be displayed here
    """
    form_model = 'group'
    form_fields = ['authority_multiply']

    def is_displayed(self):
        # displaying if there is no authority and if player is the chosen to mult
        if self.group.authority == "no authority" and self.player.id_in_group == self.group.authority_ID:
            return True
        else:
            return False

    def vars_for_template(self):
        return {
            'mult': self.group.multiplier,
            "appropiation_percent_display": str(round(self.group.appropriation_percent/2, 2)*100)+"%",
            'round_num': self.round_number
        }
    
    def before_next_page(self):
        if self.group.appropriation_percent == 0:
            self.group.auth_appropriate = False
        else:
            self.group.auth_appropriate = True


class Authority(Page):
    form_model = 'group'
    form_fields = ['auth_appropriate']

    def is_displayed(self):
        if self.group.authority != "no authority" and self.player.id_in_group == self.group.authority_ID:
            return True
        else:
            return False

    def vars_for_template(self):
        return {
            'mult': self.group.multiplier,
            'tax': self.group.tax_percent * 100, 
            'round_num': self.round_number, 
            "appropiation_percent_display": str(round(self.group.appropriation_percent/2, 2)*100)+"%"
        }


class AuthorityWaitPage(WaitPage):
    """Determines the payoff for all players based on the decision of the Authority"""
    
    def after_all_players_arrive(self):
        group = self.group
        players = group.get_players()

        # getting group parameters
        tax = self.group.tax_percent
        multiplier = self.group.multiplier
        appropriation_percent = self.group.appropriation_percent

        # setting up contribution parameters
        contributions = [p.contribution * tax for p in players]
        group.total_contribution = sum(contributions)
        print("group.total_contribution = ", group.total_contribution)
        group.total_earnings = group.total_contribution*multiplier
        print("group.total_earnings = ", group.total_earnings)
        group.appropriation = group.total_contribution*appropriation_percent*group.auth_appropriate # if no appropriation, this will be zero
        print("group.id = ", group.id_in_subsession)
        print("group.appropriation_percent = ", group.appropriation_percent)
        print("group.appropriation = ", group.appropriation)
        group.individual_share = (group.total_earnings - group.appropriation) / Constants.players_per_group

        # assigning payoffs
        for p in players: 
            if p.audit:
                p.payoff = p.income_after_audit + group.individual_share
            else:
                p.payoff = p.income_after_taxes + group.individual_share

            if p.id_in_group == group.authority_ID: # adding the appropiated amt to auth/random indv
                p.payoff += group.appropriation


class AuthorityInfo(Page):
    """Lets the other players know what decision the Authority player made."""

    def is_displayed(self):
        if self.player.id_in_group == self.group.authority_ID:
            return False
        else:
            return True

    def vars_for_template(self):
        group = self.group

        # getting group parameters
        multiplier = group.multiplier

        # displaying the choice from the authority
        if group.auth_appropriate is False:
            decision = Constants.decisions[0]
        else:
            decision = Constants.decisions[1] + " " + str(multiplier) + Constants.decisions[2] + str(round(self.group.appropriation_percent/2, 2)*100) + Constants.decisions[3]

        return {"decision": decision, 'round_num': self.round_number}


class TaxResults(Page):
    def vars_for_template(self):
        group = self.group
        player = self.player

        # impuestos cobrados
        tax = group.tax_percent
        taxcob =  tax*player.contribution 

        # storing round payoff
        self.player.round_payoff = self.player.payoff
        if self.round_number == 1:
            self.player.participant.vars["round_payoffs"] = []
        self.player.participant.vars["round_payoffs"].append(self.player.round_payoff)

        return{
            'orig': player.income_before_taxes,'total_contribution': group.total_contribution,
            'total_earnings': group.total_earnings, 'total_appropriation': group.appropriation,
            'round_num': self.round_number, 'taxcob':taxcob,'tax': tax, 'payoff': player.payoff,
            'appropiation_percent_display': str(round(self.group.appropriation_percent/2, 2)*100*group.auth_appropriate)+"%",
            'authority': group.authority
        }
    
    def before_next_page(self):
        if self.round_number == Constants.num_rounds: # choosing a payoff at random
            self.player.chosen_round = random.randint(1, Constants.num_rounds)
            chosen_round = self.player.chosen_round
            self.player.participant.payoff = self.player.participant.vars["round_payoffs"][chosen_round - 1]


class FinalResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds
    
    def vars_for_template(self):
        return {"round_num": self.round_number,
                "chosen_round": self.player.chosen_round,
                "chosen_payoff": self.player.participant.payoff}
        
        
page_sequence = [InitialWaitPage, Introduction, InstructionsB, Transcribe, ReportIncome, Audit,
                 NoAuthority,  Authority, AuthorityWaitPage, AuthorityInfo, TaxResults, FinalResults]