from itertools import combinations
import random

def generate_match_per_app(num_players, players_per_group, rounds):
    player_ids = [id for id in range(num_players + 1)]
    player_ids_pairs = list(combinations(player_ids, players_per_group))

    random.shuffle(player_ids_pairs) # randomizing pairing orders

    matching_rounds = {}
    players_to_ignore_round = {}


    # for round_num in range(1, rounds+1):
    #     matching_rounds[f"round_{round_num}"] = []
    #     players_to_ignore_round[f"round_{round_num}"] = []

    #     print(f"matching_rounds = {matching_rounds}")
    #     # storing pairings for specific player
    #     for player in range(num_players + 1):
    #         for pairing in player_ids_pairs:
    #             print(f"current player = {player}")
    #             print(f"current pairing = {pairing}")
    #             if player not in players_to_ignore_round[f"round_{round_num}"]:
    #                 if player in pairing and round_num <= rounds:
    #                     matching_rounds[f"round_{round_num}"].append(pairing)
    #                     # excluding player from being elected again in round
    #                     players_to_ignore_round[f"round_{round_num}"].append(player) 

    #                     # excluding player from being elected again in round
    #                     aux_pairing = list(pairing)
    #                     aux_pairing.remove(player)

    #                     players_to_ignore_round[f"round_{round_num}"].append(aux_pairing[0])
            
    #TODO: use players to ignore or similar variable at player level for future rounds
    return matching_rounds, players_to_ignore_round

#print(generate_match_per_app(12, 2, 4))

num_players = 6
players_per_group = 2
player_ids = [id for id in range(1, num_players + 1)]
player_ids_pairs = list(combinations(player_ids, players_per_group))
random.shuffle(player_ids_pairs)
print(f"player_ids_pairs = {player_ids_pairs}")
players_to_ignore_sub = {} # in current subsession
players_to_ignore_round = [] # in current round
matching_rounds = []

for player in range(1, num_players + 1):
    print("----- Player -----")
    print(f"current player = {player}")
    if f"player_{player}" not in players_to_ignore_sub: # adding key if not in dict
        players_to_ignore_sub[f"player_{player}"] = []
    print(f"current players_to_ignore_sub = {players_to_ignore_sub}")
    
    for pairing in player_ids_pairs:
        print("----- Pairing -----")
        print(f"current pairing = {pairing}")
        print(f"player in pairing = {player in pairing}")
        print(f"player not in players_to_ignore_round = {player not in players_to_ignore_round}")
        
        if player in pairing:
            aux_pairing = list(pairing)
            print(f"aux_pairing 1 = {aux_pairing}")
            aux_pairing.remove(player)
            print(f"aux_pairing 2 = {aux_pairing}")
            # getting partner
            partner = aux_pairing[0]

            if player not in players_to_ignore_round and partner not in players_to_ignore_round:
                matching_rounds.append(pairing)
                print(f"matching_rounds = {matching_rounds}")

                # excluding player and from being elected again in round
                print(f"players_to_ignore_round = {players_to_ignore_round}")
                
                # ignoring both players in round
                players_to_ignore_round.append(player)
                players_to_ignore_round.append(partner)
                
                # ignoring both players in subsession for future partners
                ## ignoring player
                players_to_ignore_sub[f"player_{player}"].append(partner)
                print(f"players_to_ignore_sub = {players_to_ignore_sub}")

                ## ignoring partner
                if f"player_{partner}" not in players_to_ignore_sub: # adding key if not in dict
                    players_to_ignore_sub[f"player_{partner}"] = []
                players_to_ignore_sub[f"player_{partner}"].append(player)
                print(f"players_to_ignore_sub = {players_to_ignore_sub}")

print(f"final matching_rounds = {matching_rounds}")
print(f"final players_to_ignore_round = {players_to_ignore_round}")
print(f"final players_to_ignore_sub = {players_to_ignore_sub}")