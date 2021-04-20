from itertools import combinations
import random, json, os

random.seed(123)

def all_round_matchings(num_players, players_per_group, num_rounds):
    """
    Generates matching file for an specific number of rounds with 
    the same number of players and players per group

    Input: number of players (int), players per group (int), number of rounds (int) 
    Output: matchings for all the session (dict), players to ignore 
    for future matchings (dict)
    """
    # getting player pairs
    player_ids = [id for id in range(1, num_players + 1)]
    player_ids_pairs = list(combinations(player_ids, players_per_group))
    
    # print(f"player_ids_pairs = {player_ids_pairs}")
    players_to_ignore_sub = {} # in current subsession
    matching_rounds = {}
    
    # generating matchings per round
    for round_num in range(1, num_rounds + 1):
        # print("----- Round -----")
        # print(f"current round = {round_num}")
        matching_rounds[f"round_{round_num}"] = []
        players_to_ignore_round = [] # in current round

        print("Starting while loop")
        for player in range(1, num_players + 1):
            #print("----- Player -----")
            # print(f"current player = {player}")
            if f"player_{player}" not in players_to_ignore_sub: # adding key if not in dict
                players_to_ignore_sub[f"player_{player}"] = []
            # print(f"current players_to_ignore_sub = {players_to_ignore_sub}")
            
            if player not in players_to_ignore_round:
                # finding the first pairing in which player appears
                pairing_found = False
                for pairing in player_ids_pairs:
                    #print("----- Pairing -----")
                    # print(f"current pairing = {pairing}")
                    # print(f"player in pairing = {player in pairing}")
                    # print(f"player not in players_to_ignore_round = {player not in players_to_ignore_round}")
                    
                    # checking if pairing already considered in any previous round
                    pairing_already_considered = False
                    for matching in matching_rounds.values():
                        # print(f"current checked matchings = {matching}")
                        # checking per each round pairings
                        if pairing in matching:
                            pairing_already_considered = True
                        # if already considered, break
                        if pairing_already_considered:
                            break

                    # if first round or (any other round and pairing is not in a previous matching)
                    if not pairing_already_considered:
                        if player in pairing:
                            aux_pairing = list(pairing)
                            # print(f"aux_pairing 1 = {aux_pairing}")
                            aux_pairing.remove(player)
                            # print(f"aux_pairing 2 = {aux_pairing}")
                            # getting partner
                            partner = aux_pairing[0]

                            # storing pairing if players shouldn't be ignored
                            if partner not in players_to_ignore_round:
                                matching_rounds[f"round_{round_num}"].append(pairing)
                                # print(f"matching_rounds[f'round_{round_num}'] = {matching_rounds[f'round_{round_num}']}")

                                # excluding player and from being elected again in round
                                # print(f"players_to_ignore_round = {players_to_ignore_round}")
                                
                                # ignoring both players in round
                                players_to_ignore_round.append(player)
                                players_to_ignore_round.append(partner)
                                
                                # ignoring both players in subsession for future partners
                                ## ignoring player
                                players_to_ignore_sub[f"player_{player}"].append(partner)
                                # print(f"players_to_ignore_sub = {players_to_ignore_sub}")

                                ## ignoring partner
                                if f"player_{partner}" not in players_to_ignore_sub: # adding key if not in dict
                                    players_to_ignore_sub[f"player_{partner}"] = []
                                players_to_ignore_sub[f"player_{partner}"].append(player)
                                # print(f"players_to_ignore_sub = {players_to_ignore_sub}")

                                ## declaring that pairing was found for player
                                pairing_found = True
                    
                    if pairing_found:
                        break
            
            print(f"matching_rounds[f'round_{round_num}'] = {matching_rounds[f'round_{round_num}']}")
            print(f"Length of len(matching_rounds[f'round_{round_num}']) = {len(matching_rounds[f'round_{round_num}'])}")

    print(f"final matching_rounds = {matching_rounds}")
    print(f"final players_to_ignore_round = {players_to_ignore_round}")
    print(f"final players_to_ignore_sub = {players_to_ignore_sub}")
    return matching_rounds, players_to_ignore_sub

#TODO: generate single round matching using prev matchings as input
#TODO: generate json with every app matchings
matches, ignored = all_round_matchings(num_players=12, players_per_group=2, num_rounds=20)

def matcher_single_round(num_players, players_per_group, players_to_ignore):
    """
    Generates matching file for an app with 1 round with 
    the same number of players and players per group. Takes
    into account players to be ignored in previous matches

    Input: number of players (int), players per group (int), players to ignore
    for current matchings (dict)
    Output: matchings for all the session (dict), players to ignore 
    for future matchings (dict)
    """
    # getting player pairs
    player_ids = [id for id in range(1, num_players + 1)]
    player_ids_pairs = list(combinations(player_ids, players_per_group))
    players_to_be_ignored = [] # players that should be ignored for current matchings

    random.shuffle(player_ids_pairs)
    
    matching_rounds = []

    # obtaining pairings per player
    for player in range(1, num_players + 1):
       # print("----- Player -----")
       # print(f"current player = {player}")

       # print(f"player not in players_to_be_ignored = {player not in players_to_be_ignored}")
        if player not in players_to_be_ignored:
            for grouping in player_ids_pairs:
               # print("----- Grouping -----")
               # print(f"current grouping = {grouping}")
               # print(f"player in grouping = {player in grouping}")
            
                grouping_already_considered = False
               # print(f"matching_rounds length = {len(matching_rounds)}")
                if len(matching_rounds) != 0:
                    for matching in matching_rounds:
                       # print(f"current checked matching = {matching}")
                        # checking per each round grouping
                        if grouping in matching:
                            grouping_already_considered = True
                        # if already considered, break
                        if grouping_already_considered:
                            break
                
               # print(f"grouping_already_considered = {grouping_already_considered}")
                if not grouping_already_considered:
                    if player in grouping:
                        # getting partners
                        partners = list(grouping)
                       # print(f"partners = {partners}")
                        partners.remove(player)
                       # print(f"partners = {partners}")
                        
                        # checking if a player that should be ignored is in group
                        ignored_in_group = False
                        
                       # print("---- Checking if partners should be ignored ----")
                        for partner in partners:
                           # print(f"partner = {partner}")
                           # print(f"partner in players_to_ignore[f'player_{player}'] = {partner in players_to_ignore[f'player_{player}']}")    
                            if partner in players_to_ignore[f"player_{player}"] or partner in players_to_be_ignored:
                                ignored_in_group = True
                            if ignored_in_group:
                                break
                        
                        # storing grouping if players shouldn't be ignored
                       # print(f"not ignored_in_group = {not ignored_in_group}")
                        if not ignored_in_group:
                            matching_rounds.append(grouping)
                           # print(f"matching_rounds = {matching_rounds}")

                            # excluding player and from being elected again in round
                           # print(f"players_to_be_ignored = {players_to_be_ignored}")
                            
                            # ignoring both players in round
                            players_to_be_ignored.append(player)
                           # print(f"players_to_be_ignored = {players_to_be_ignored}")
                            players_to_be_ignored = players_to_be_ignored + partners
                           # print(f"players_to_be_ignored = {players_to_be_ignored}")

                if player in players_to_be_ignored:
                    break

   # print("--- Matching rounds ---")
   # print(f"matching_rounds = {matching_rounds}")
   # print(f"players_to_be_ignored = {players_to_be_ignored}")
    return matching_rounds, players_to_be_ignored

# matches, ignored = all_round_matchings(num_players=12, players_per_group=2, num_rounds=6)
# matcher_single_round(12, 4, ignored)


def matching_to_json(num_players=12, players_per_group=2, same_num_rounds=6):
    """
    This function will create a dictionary with the matchings for each app per round

    Input: number of players (int), players per group (int), number of rounds for apps with same
    random matching system (int)
    Output: 
    *dictionary file with matchings for all apps (json)
    """

    app_1_name = "trust"
    app_2_name = "dictator"
    last_app_name = "public_goods"

    # app_1_name = input("Name of same num_round app 1: ")
    # app_2_name = input("Name of same num_round app 2: ")
    # last_app_name = input("Name of last app: ")
    
    # last_app_num_rounds = input("Last app rounds: ")
    last_app_num_rounds = 3

    session_matching = {} # matchings for whole session

    # obtaining first 2 apps matchings
    first_app_matches, ignored = all_round_matchings(num_players, players_per_group, same_num_rounds)
    
    # setting first 2 apps matchings
    print(f"first_app_matches = {first_app_matches}")
    session_matching[app_1_name] = {}
    session_matching[app_2_name] = {}
    half_of_rounds = int(same_num_rounds/2)
    for round_num in range(1, half_of_rounds + 1):
        session_matching[app_1_name][f"round_{round_num}"] = first_app_matches[f"round_{round_num}"]
        session_matching[app_2_name][f"round_{round_num}"] = first_app_matches[f"round_{round_num + half_of_rounds}"]
    
    # setting last app matching
    session_matching[last_app_name] = {}
    last_app_matchings, to_ignore = matcher_single_round(12, 4, ignored)
    # appending the same matching for all rounds
    round_num = 1
    while round_num <= last_app_num_rounds:
        # print(f"last_app_matchings = {last_app_matchings}")
        session_matching[last_app_name][f"round_{round_num}"] = last_app_matchings
        round_num += 1

    path = str(input(
       "\n[1] Please, input the path where you want your oTree matching file "
       "(e.g. D:/otree_project1/config/ or ./config/): \n"))

    file_name = str(input("\n[2] Input your preferred name for the matching file " 
                         "(don't write the extension):\n"))

    file_path_name = path + file_name
    temp_extension = '.txt'
    # generating our temp matching file
    with open(file_path_name + temp_extension, 'a+') as target_file:
        json.dump(session_matching, target_file, indent=2)
    
    text = open(file_path_name + temp_extension, "r") # txt file to be reformated for json
    lines = text.readlines()
    string_output = "".join(lines)

    with open(file_path_name + '.json', 'a+') as target_file:
        target_file.write(string_output)

    text.close()
    os.remove(file_path_name + temp_extension)  # erasing the tmp

#matching_to_json()