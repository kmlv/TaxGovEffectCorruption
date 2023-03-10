from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.Introduction
        
        yield pages.InstructionsB

        yield (pages.Transcribe, {"transcribed_text": self.player.refText}) # yielding exact text for avoiding wait times

        yield (pages.ReportIncome, {"contribution": 10})

        if self.player.audit == 1:
            yield pages.Audit

        approp_test_value = False # true for first half of rounds
        if self.player.id_in_group == self.group.authority_ID:
            # no authority validation
            if self.group.authority == "no authority":
                if self.group.appropriation_percent != 0:
                    yield (pages.NoAuthority, {"auth_appropriate": True})
                else:
                    yield (pages.NoAuthority, {"auth_appropriate": False})
            
            # authority validation
            elif self.group.authority != "no authority":     
                if self.round_number > round(Constants.num_rounds/2):
                    approp_test_value = True # false for second half
                yield (pages.Authority, {"auth_appropriate": approp_test_value})
            else:
                print("Error with authority validation")

        if self.player.id_in_group != self.group.authority_ID:
            yield pages.AuthorityInfo
        
        yield pages.TaxResults

        if self.round_number == Constants.num_rounds:
            yield pages.FinalResults
