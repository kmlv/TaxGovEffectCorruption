import random
total_players = 15
players_per_group = 5

# getting all players ids (assumption: total am. of players is even)
player_ids = [id for id in range(1, total_players + 1)]

# Shuffle players randomly so that they can end up in any group
random.shuffle(player_ids)

print("player_ids: ", player_ids)

# creating player groups of size players_per_group
group_matrix = []
group_list = []
index_id = 1
for id in player_ids:
    
    # creating our group
    group_list.append(id)

    # updating matrix and creating new group list
    if (index_id) % players_per_group == 0: 
        group_matrix.append(group_list)
        group_list = []

    index_id += 1

print("group_matrix: ", group_matrix)
