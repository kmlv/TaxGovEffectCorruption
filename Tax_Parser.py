import pandas as pd 

data = pd.read_csv("session2_parsed.csv") # data acumulada

new_session = pd.read_csv(r"C:\Users\Sergio\Downloads\sesion3.csv") # new session data

#### Parser ####

ids = new_session[
    [
        'participant.code',
        'participant.label',
    ]
] 

ids.columns = ['code','label']

dictator = new_session[
    [
        'dictator.1.player.dictator',
        'dictator.1.player.id_in_group',
        'dictator.1.group.id_in_subsession',
        'dictator.1.player.kept',
        'dictator.1.group.group_kept',
        'dictator.1.player.payoff'
    ]
] 

dictator.columns = [
    'dictator.dictator',
    'dictator.id_in_group',
    'dictator.group.id',
    'dictator.kept',
    'dictator.group_kept',
    'dictator.payoff'
    ]

# trust
sent_back_strat = ["trust.1.player.sent_back_amount_strategy_"+str(i)
                   for i in range(9,100,9) ]

variables = [
        'trust.1.player.trustor',
        'trust.1.player.sent_amount_strategy',
        'trust.1.player.trustee',
        'trust.1.player.id_in_group',
        'trust.1.group.id_in_subsession',
    ] + sent_back_strat +  [
        'trust.1.group.sent_amount',
        'trust.1.group.sent_back_amount',
        'trust.1.player.payoff'
    ]

trust = new_session[variables] 

sent_back_strat_col = ["trust.sent_back_amount_strat_"+str(i)
                   for i in range(9,100,9) ]

trust.columns = [
        'trust.trustor',
        'trust.sent_amount_strategy',
        'trust.trustee',
        'trust.id_in_group',
        'trust.group.id',
    ] + sent_back_strat_col +  [
        'trust.sent_amount',
        'trust.sent_back_amount',
        'trust.payoff'
    ]

# public goods
public_goods = new_session[
    [
        'public_goods.1.player.contribution',
        'public_goods.1.player.id_in_group',
        'public_goods.1.group.id_in_subsession',
        'public_goods.1.group.total_contribution',
        'public_goods.1.group.individual_share',
        'public_goods.1.player.payoff'
    ]
]  

public_goods.columns = [
    'public_goods.contribution',
        'public_goods.id_in_group',
        'public_goods.group.id',
        'public_goods.total_contribution',
        'public_goods.individual_share',
        'public_goods.payoff'
]

# coin tossing
variables = []
for i in range(1,6):
    temp = [
    'coin_tossing.'+str(i)+'.player.heads_or_tails',
    'coin_tossing.'+str(i)+'.player.number_of_heads',
    'coin_tossing.'+str(i)+'.player.real_coin_value',
    'coin_tossing.'+str(i)+'.player.player_is_lying',
    'coin_tossing.'+str(i)+'.player.payoff']
    variables += temp
    
coin_tossing = new_session[variables] 

coin_tossing['Num_Lies'] = sum([coin_tossing['coin_tossing.'+str(i)+'.player.player_is_lying'] for i in range(1,6)])
coin_tossing['%_Lies'] = coin_tossing['Num_Lies']*100/5
coin_tossing['Payoff_Coin_Tossing'] = sum([coin_tossing['coin_tossing.'+str(i)+'.player.payoff'] for i in range(1,6)])

variables = ['Num_Lies','%_Lies','Payoff_Coin_Tossing']
coin_tossing = coin_tossing[variables]

coin_tossing.columns = [variables]

final_data = pd.concat([ids,dictator,trust,public_goods,coin_tossing], axis=1)

#### End Parser ####

### Formatting columns ### 

variables = final_data.columns.tolist()

for element in range(len(variables)): 
    variables[element] = variables[element][0].replace(".","_") if type(variables[element]) is tuple else variables[element].replace(".","_")

final_data.columns = variables

### End Formatting columns ### 

acum_data = pd.concat([data,final_data]) # concat all data sessions with the new one

acum_data.drop_duplicates(inplace = True) 

acum_data.to_csv("session3_parsed.csv", index=False) #exporting the new data

