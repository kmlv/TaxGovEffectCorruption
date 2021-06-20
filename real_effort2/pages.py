from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, levenshtein, distance_and_ok
from django.conf import settings
import PIL
from PIL import Image, ImageDraw, ImageFont
import math
from random import *
import random
import string
from .config import data_grps as data_all_groups

def get_group_data(group_id_in_subsession, parameter):
    """
    Gets the required parameter for an specific group

    Input: group id in subsession (int), parameter (string)
    Output: parameter (int/str/etc)
    """

    group_id = group_id_in_subsession
    group_data = data_all_groups[f"group_{group_id}"]
    return group_data[f"{parameter}"]


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

def generateText1(difficulty):
    """This method generates randomized garbled text whose difficulty to transcribe is based on the difficulty paramaeter
    (between 1 to 3) that's passed in."""

    min_char = 4 * difficulty
    max_char = min_char + 6
    allchar = string.ascii_lowercase + string.digits + string.punctuation
    vowels = ('a','e','i','o','u')

    #generated = "$eub:uuwhui eiu,u.ead^)ie{hp/irle.eug aw2x~auao`u.pi-[n+eaoqej."
    generated=""

    if(difficulty == 1):
        allchar = string.ascii_lowercase
    if(difficulty == 2):
        allchar = string.ascii_lowercase + string.digits
    for i in range(10):
        for i in range(5):
             allchar += vowels[i]
    
    while(len(generated) < 70 - max_char):
        add = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
        generated += (add +".")

    return generated


def generateText2(difficulty):
    """This method generates randomized garbled text whose difficulty to transcribe is based on the difficulty paramaeter
    (between 1 to 3) that's passed in."""

    min_char = 4 * difficulty
    max_char = min_char + 6
    allchar = string.ascii_lowercase + string.digits + string.punctuation
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


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    
    def is_displayed(self):
        if (self.round_number == 1):
            return True
        else:
            return False

    
class InstructionsB(Page):
    """Description of the game block"""
    
    # TODO: update instructions
    def is_displayed(self):
        if (self.round_number == 1):
            return True

        return False
    
    
class Transcribe1(Page):
    """First transcription task that's shown to the player that is merely for practice and does not determine the ratio
    for the player's starting income"""
    form_model = 'player'
    form_fields = ['transcribed_text2']

    def is_displayed(self):
        self.player.refText = generateText1(self.session.vars["config"][0][self.round_number - 1]["difficulty"])
        # Don't display this Transcribe2 page if the "transcription" value in
        # the dictionary representing this round in config.py is False
        print("Inside Transcribe1 page")
        print("Transcription for this round is: " + str(self.session.vars["config"][0][self.round_number - 1]["transcription"]))

        if (self.session.vars["config"][0][self.round_number - 1]["transcription"] == False):
            self.player.ratio = 1
            return False


        """
        # Don't display this Transcribe1 page for each player who has completed
        # the second transcription task
        for p in self.player.in_all_rounds():
            if(p.transcriptionDone):
                return False
        """

        return True

    def vars_for_template(self):
        
        writeText(self.player.refText, 'real_effort2/static/real_effort2/paragraphs/{}.png'.format(self.player.id_in_group))
        return {
            'image_path': 'real_effort2/paragraphs/{}.png'.format(1),
            'reference_text': self.player.refText,
            'debug': settings.DEBUG,
            'round_num': self.round_number,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rates[0]),
        }

    def before_next_page(self):
        """Initialize payoff to have a default value of 0"""
        self.player.payoff = 0


class Transcribe2(Page):
    """Second transcription task that's shown to the player that determines the ratio sfor the player's starting income"""
    form_model = 'player'
    form_fields = ['transcribed_text']

    # la transcripcion se aproxima al entero mas cercano si la parte decimal es mayor a .5 (no mayor igual)
    # Don't display this Transcribe2 page if the "transcription" value in
    # the dictionary representing this round in config.py is False
    def is_displayed(self):
        print("Inside Transcribe2 page")
        print("Transcription for this round is: " + str(self.session.vars["config"][0][self.round_number - 1]["transcription"]))

        if (self.session.vars["config"][0][self.round_number - 1]["transcription"] == False):
            return False

        """
        # Don't display this Transcribe2 page for each player who has completed
        # the first transcription task
        for p in self.player.in_all_rounds():
            if(p.transcriptionDone):
                return False
        """

        self.player.refText = generateText2(self.session.vars["config"][0][self.round_number - 1]["difficulty"])

        return True

    def vars_for_template(self):
        
        writeText(self.player.refText, 'real_effort2/static/real_effort2/paragraphs/{}.png'.format(2))
        return {
            'image_path': 'real_effort2/paragraphs/{}.png'.format(2),
            'reference_text': self.player.refText,
            'debug': settings.DEBUG,
            'required_accuracy': 100 * (1 - Constants.allowed_error_rates[1]),
            'round_num': self.round_number
        }

    def transcribed_text_error_message(self, transcribed_text):
        """Determines the player's transcription accuracy."""

        reference_text = self.player.refText
        allowed_error_rate = Constants.allowed_error_rates[1]
        distance, ok = distance_and_ok(transcribed_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance = distance
            self.player.ratio = 1 - distance / Constants.maxdistance2
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "Para avanzar, debes transcribir más caracteres similares a la transcripción original."

    def before_next_page(self):
        self.player.ratio = 1 - self.player.levenshtein_distance / len(self.player.refText)
        self.player.income *= self.player.ratio
        self.player.payoff = 0
        self.player.transcriptionDone = True


class ReportIncome(Page):
    """Page where the player reports his/her income"""
    form_model = 'player'
    form_fields = ['contribution']

    def contribution_max(self):
        """Dynamically sets the maximum amount of each player's income that he/she can report"""
        return self.player.income

    def vars_for_template(self):
        # If transcription mode is set to true for this round, set the player's income according
        # to their transcription accuracy
        self.player.orig_income = self.player.income

        if self.player.ratio == 1 and self.session.vars["config"][0][self.round_number - 1]["transcription"] == True:
            for p in self.player.in_all_rounds():
                if p.ratio < 1:
                    self.player.ratio = p.ratio
                    self.player.income *= p.ratio
                    break

        displaytax = config[0][self.round_number - 1]["tax"] * 100
        display_ratio = round(self.player.ratio * 100, 1)
        display_income = self.player.income

        return {'ratio': self.player.ratio, 'income': self.player.income, 'tax': displaytax,
                'flag': config[0][self.round_number - 1]["transcription"],
                'mult': config[0][self.round_number - 1]["multiplier"],
                'display_ratio': display_ratio, 'endowment': self.player.endowment,
                'display_income': display_income, 'transcribe_on': self.group.transcription_required,
                'round_num': self.round_number
        }

    def before_next_page(self):
        self.group.appropriation = 0
        if random.randint(0, 1) == 0:
            self.player.audit = True
        else:
            self.player.audit = False


class Audit(Page):
    """Alerts a player (if he/she has been chosen) that they have been audited and informs them whether their actual
    and reported income match. If not, they incur a penalty that's deducted from their remaining income after taxes
    are deducted."""
    def is_displayed(self):
       # return self.player.audit
       if self.player.audit2 == 1:
           return True
       else:
           return False

    def vars_for_template(self):
        player = self.player

        # If player's reported income and actual income don't match
        if player.contribution != player.income:
            player.income_before_taxes = player.income # check if this works
            player.income = (1 - self.group.penalty_percent) * (player.income - (self.group.tax_percent * player.contribution))

            return {
                'fail': True,
                'correctIncome': player.income_before_taxes,
                'reportedIncome': player.contribution,
                'newIncome': round(player.income, 1),
                'penalty': self.group.penalty_percent * 100,
                'round_num': self.round_number
            }
        else:
            return {
                'fail': False, 'round_num': self.round_number
            }


# TODO: refactor all previous pages for parameters usage
class resultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        group = self.group

        # Generate a random player ID to determine who will be the authority
        # TODO: create a mechanism to determine who could be an authority
        # TODO: assign (non)benevolent authority depending on the treatment and config.py
        group.authority_ID = random.randint(1, Constants.players_per_group)


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
            'appropriation_percent': self.group.appropriation_percent * 100,
            'round_num': self.round_number
        }


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
            'display_app_percent': self.group.appropriation_percent * 100
        }


class AuthorityWaitPage(WaitPage):
    """Determines the payoff for all players based on the decision of the Authority"""
    def after_all_players_arrive(self):
        config = self.session.vars["config"]
        group = self.group
        players = group.get_players()

        mode_num: object = config[0][self.round_number - 1]["mode"]
        tax = config[0][int(self.round_number - 1)]["tax"]
        multiplier = config[0][self.round_number - 1]["multiplier"]
        appropriation_percent = config[0][self.round_number - 1]["appropriation_percent"]

        if mode_num == 1:
            contributions = [p.contribution * tax for p in players]
            group.total_contribution = sum(contributions)
            group.total_earnings = group.total_contribution*multiplier

            group.individual_share = group.total_earnings / Constants.players_per_group

            for p in players:
                p.payoff = p.income - (tax * p.contribution) + group.individual_share

        elif (mode_num == 2 or mode_num == 3) and not group.auth_appropriate:
            contributions = [p.contribution * tax for p in players]
            group.total_contribution = sum(contributions)
            group.total_earnings = group.total_contribution*multiplier

            group.individual_share = group.total_earnings / Constants.players_per_group

            for p in players:
                p.payoff = p.income - (tax * p.contribution) + group.individual_share

        # Mode 2, Authority Mode 2, Button 2 (Appropriation)
        else:
        #elif mode_num == 3 and not group.auth_appropriate:
            contributions = [p.contribution * tax for p in players]
            group.total_contribution = sum(contributions)
            group.total_earnings = group.total_contribution*multiplier

            group.appropriation = appropriation_percent * group.total_earnings
            group.individual_share = (group.total_earnings*(1-appropriation_percent)) / Constants.players_per_group

            for p in players:
                if p.id_in_group == group.authority_ID:
                    p.payoff = p.income - (tax * p.contribution) + group.individual_share + group.appropriation
                else:
                    p.payoff = p.income - (tax * p.contribution) + group.individual_share


class AuthorityInfo(Page):
    # TODO: update for new modes of (no) authority
    """Lets the other players know what decision the Authority player made."""
    def is_displayed(self):
        group = self.group

        if (self.player.id_in_group == group.authority_ID):
            return False
        else:
            return True

    def vars_for_template(self):
        config = self.session.vars["config"]
        group = self.group
        pgCode = getPageCode(self)

        mode_num = config[0][self.round_number - 1]["mode"]
        multiplier = config[0][self.round_number - 1]["multiplier"]
        tax = config[0][self.round_number - 1]["tax"]
        appropriation_percent = config[0][self.round_number - 1]["appropriation_percent"]

        if(mode_num == 1 and group.authority_multiply):
            decision = Constants.decisions[1] + " " + str(multiplier) + "."
        elif(mode_num == 1 and not group.authority_multiply):
            decision = Constants.decisions[0]
        elif(mode_num == 2 and not group.auth_appropriate):
            decision = Constants.decisions[1] + " " + str(multiplier) + " ."
        else:
            decision = Constants.decisions[1] + " " + str(multiplier) + Constants.decisions[2] + str(appropriation_percent * 100) + Constants.decisions[3]

        return {"mode": mode_num, "decision": decision, 'pgCode': pgCode, 'round_num': self.round_number}


class TaxResults(Page):
    def vars_for_template(self):
        config = self.session.vars["config"]
        pgCode = getPageCode(self)
        group = self.group
        players = group.get_players()
        player = self.player
        share = self.group.total_earnings / Constants.players_per_group
        appropriation_percent = config[0][self.round_number - 1]["appropriation_percent"]
        display_appropriation = appropriation_percent * 100 # formatting the percent
        mode_num = config[0][self.round_number - 1]["mode"]
        tax = config[0][int(self.round_number - 1)]["tax"]
        #impuestos cobrados:
        taxcob = config[0][int(self.round_number - 1)]["tax"]*player.contribution
        #penalidad:
        pen =  player.contribution*90/100
        multiplier = config[0][self.round_number - 1]["multiplier"]
        orig = self.player.orig_income

        if mode_num == 1:
            contributions = [p.contribution * tax for p in players]
            group.total_contribution = sum(contributions)
            group.total_earnings = group.total_contribution * multiplier

            group.individual_share = group.total_earnings / Constants.players_per_group

            for p in players:
                p.payoff = p.income - (tax * p.contribution) + group.individual_share

        elif (mode_num == 2 or mode_num == 3) and not group.auth_appropriate:
            contributions = [p.contribution * tax for p in players]
            group.total_contribution = sum(contributions)
            group.total_earnings = group.total_contribution * multiplier

            group.individual_share = group.total_earnings / Constants.players_per_group

            for p in players:
                p.payoff = p.income - (tax * p.contribution) + group.individual_share

        # Mode 2, Authority Mode 2, Button 2 (Appropriation)
        else:
            contributions = [p.contribution * tax for p in players]
            group.total_contribution = sum(contributions)
            group.total_earnings = group.total_contribution * multiplier

            group.appropriation = appropriation_percent * group.total_earnings
            group.individual_share = (group.total_earnings * (1 - appropriation_percent)) / Constants.players_per_group

            for p in players:
                if (p.id_in_group == group.authority_ID):
                    p.payoff = p.income - (tax * p.contribution) + group.individual_share + group.appropriation
                else:
                    p.payoff = p.income - (tax * p.contribution) + group.individual_share

        return{
            'orig': orig,'total_contribution': self.group.total_contribution,'total_earnings': self.group.total_earnings,
            'total_appropriation':self.group.appropriation, 'pgCode': pgCode, 'round_num': self.round_number,'mode':mode_num, 'taxcob':taxcob,'tax': tax,'payoff': self.player.payoff,
        }

page_sequence = [Introduction, InstructionsB, Transcribe2, ReportIncome, Audit, resultsWaitPage,
                 NoAuthority,  Authority, AuthorityWaitPage, AuthorityInfo, TaxResults]

#page_sequence = [Introduction, InstructionsB, Transcribe2, ReportIncome, Audit, resultsWaitPage,
#                 AuthorityMaster, AuthorityWaitPage, AuthorityInfo, TaxResults]
