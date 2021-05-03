# CONFIG PARAMETERS LEEX EXPERIMENTS SET 2017

# Prelims
paid_game_display = {
    'ultimatum': 'Bloque UG',
    'public_goods': 'Bloque PG',
    'trust': 'Bloque TG',
    'guess_two_thirds': 'Bloque BC',
}


# GAME PARAMETERS

# GAME ORDER. Change every session!
app_sequence = ['public_goods', 'trust', 'ultimatum', 'guess_two_thirds', 'payment_info', 'survey']
#
# participation_fee (soles)
participation_fee = 5


# # ultimatum game  params
UG_number_rounds = 10
UG_endowment = 20
#
# # primer engargo mg params
PEMG_number_rounds = 10
#
# # public goods params
PG_number_rounds = 10
PG_endowment = 8
#
# # trust game
TG_number_rounds = 10
TG_endowment = 8
#
# # guessing game
BC_number_rounds = 10
BC_jackpot = 20



# paid_game in ['ultimatum', 'public_goods', 'trust', 'guess_two_thirds']
paid_game = 'trust'
paid_round = 5






##################################################################################
# Order Record

# Setp 6 at 1pm:
# ['ultimatum', 'public_goods', 'trust', 'guess_two_thirds', 'payment_info', 'survey']
# paid: PG, t=2


# Setp 6 at 5pm:
# ['public_goods', 'trust', 'ultimatum', 'guess_two_thirds', 'payment_info', 'survey']
# paid: UG, t=5





##################################################################################

## TESTING PARAMS  GAME PARAMETERS

# GAME ORDER. Change every session!
#app_sequence = [ 'ultimatum', 'trust',  'payment_info', 'survey']
#
# participation_fee (soles)
#participation_fee = 5

#num_testing_rounds = 2


# ultimatum game  params
#UG_number_rounds = num_testing_rounds
#UG_endowment = 20

# public goods params
#PG_number_rounds = num_testing_rounds
#PG_endowment = 8

# trust game
#TG_number_rounds = num_testing_rounds
#TG_endowment = 8

# guessing game
#BC_number_rounds = num_testing_rounds
#BC_jackpot = 20

# # paid_game must live in ['ultimatum', 'public_goods', 'trust', 'guess_two_thirds']
#paid_game = 'ultimatum'
#paid_round = 2
