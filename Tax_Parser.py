import pandas as pd 

data = pd.read_csv("data_acum16.csv", header = [0,1]) # data acumulada

new_session = pd.read_csv(r"C:\Users\Sergio\Downloads\sesion4.csv") # new session data

#### Parser ####

ids = new_session[
    [
        'participant.code',
        'participant.label',
    ]
] 

columns_names = [
    'Code',
    'Label',
]

header = ['Participant']*2
ids.columns = [header,columns_names]

dictator = new_session[
    [
        'dictator.1.player.dictator',
        'dictator.1.player.kept',
        'dictator.1.group.group_kept',
        'dictator.1.player.payoff'
    ]
] 

columns_names = [
    'Dictador',
    'Decisión',
    'Resultado',
    'Payoff_Dictator'
]

header = ['Dictator']*4
dictator.columns = [header,columns_names] 

# trust
sent_back_strat = ["trust.1.player.sent_back_amount_strategy_"+str(i)
                   for i in range(9,100,9) ]

variables = [
        'trust.1.player.trustor',
        'trust.1.player.sent_amount_strategy',
        'trust.1.player.trustee',
    ] + sent_back_strat +  [
        'trust.1.group.sent_amount',
        'trust.1.group.sent_back_amount',
        'trust.1.player.payoff'
    ]
trust = new_session[variables] 

labels = {
    'trust.1.player.trustor':'trustor',
        'trust.1.player.sent_amount_strategy':'sent_amount_strategy',
        'trust.1.player.trustee':'trustee',
    'trust.1.group.sent_amount':'sent_amount',
        'trust.1.group.sent_back_amount':'sent_back_amount',
        'trust.1.player.payoff':'Payoff_Trust'
}

header = ['Trust']*17
trust.columns = [header,variables]
trust = trust.rename(columns = labels) 

# public goods
public_goods = new_session[
    [
        'public_goods.1.player.contribution',
        'public_goods.1.group.total_contribution',
        'public_goods.1.group.individual_share',
        'public_goods.1.player.payoff'
    ]
] 

columns_names = [
    'Contribution',
    'Total Contribution',
    'Individual Share',
    'Payoff_Public_Goods'
]

header = ['Public_Goods']*4
public_goods.columns = [header,columns_names]  

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

coin_tossing['Num Lies'] = sum([coin_tossing['coin_tossing.'+str(i)+'.player.player_is_lying'] for i in range(1,6)])
coin_tossing['% Lies'] = coin_tossing['Num Lies']*100/5
coin_tossing['Payoff_Coin_Tossing'] = sum([coin_tossing['coin_tossing.'+str(i)+'.player.payoff'] for i in range(1,6)])

variables = ['Num Lies','% Lies','Payoff_Coin_Tossing']
coin_tossing = coin_tossing[variables]

header = ['Coin_Tossing']*3
coin_tossing.columns = [header,variables]

final_data = pd.concat([ids,dictator,trust,public_goods,coin_tossing], axis=1)

acum_data = pd.concat([data,final_data]) # concat all data sessions with the new one

#### End Parser ####

acum_data.to_csv("data_updated.csv", mode="a",index=False) #exporting the new data

