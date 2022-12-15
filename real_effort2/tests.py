from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield pages.Introduction
        
        yield pages.InstructionsB

        yield (pages.Transcribe2, {"transcribed_text2": self.player.refText}) # yielding exact text for avoiding wait times

        yield (pages.ReportIncome, {"contribution": 10})

        # no authority validation
        if self.group.authority == "no authority" and self.player.id_in_group == self.group.authority_ID:
            yield (pages.NoAuthority, {"authority_multiply": True})
        
        # authority validation
        if self.group.authority != "no authority" and self.player.id_in_group == self.group.authority_ID:
            approp_test_value = True # true for first half of rounds
            if self.round_number > round(Constants.num_rounds/2):
                approp_test_value = False # false for second half
            yield (pages.Authority, {"auth_appropriate": approp_test_value})

        yield pages.AuthorityInfo
        yield pages.TaxResults
