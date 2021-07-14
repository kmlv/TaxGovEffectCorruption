import random

# Dictionary Format: endowment, multiplier, tax, transcription, authority mode, transcription difficulty, spanish toggle,
##            audit penalty, appropriation percent, shuffle
# Each dictionary entry represents the data values for 1 round

# data = [
#     [
#         {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
#          "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
#         {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
#          "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
#         {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 1, "spanish": True,
#          "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
#         {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True,
#          "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False}
#     ]
#     ]

#TODO: edit data_grps for groups with no authority
data_grps = {
            'group_1': {
                        'first_half': {
                                        "end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, 'tag': 'BA', 
                                        "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.5,
                                        'authority': 'benevolent'
                                      },
                        'second_half': {
                                        "end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, 'tag': 'EA',
                                        "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.5, 
                                        'authority': 'embezzlement'
                                      },
                       },
            'group_2': {
                        'first_half': {
                                        "end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, 'tag': 'EA', 
                                        "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.5, 
                                        'authority': 'embezzlement'
                                      },
                        'second_half': {
                                        "end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, 'tag': 'BA',
                                        "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.5, 
                                        'authority': 'benevolent'
                                      },
                       },
            'group_3': {
                        'first_half': {
                                        "end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, 'tag': 'DTA', 
                                        "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0, 
                                        'authority': 'no authority'
                                      },
                        'second_half': {
                                        "end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, 'tag': 'STA',
                                        "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.5, 
                                        'authority': 'no authority'
                                      },
                       },
            'group_4': {
                        'first_half': {
                                        "end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, 'tag': 'STA', 
                                        "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.5, 
                                        'authority': 'no authority'
                                      },
                        'second_half': {
                                        "end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, 'tag': 'DTA',
                                        "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0, 
                                        'authority': 'no authority'
                                      },
                       },
            }

data_au = [
    [
    {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.5, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.5, "shuffle": False},
    ]
    ]

data_nau = [
    [
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.5, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.5, "shuffle": False}
    ]
    ]

num_rounds = 4


def grouping_algorithm(total_players, players_per_group):
    """
    creates groups of size `players_per_group` for `total_players`

    input: total amount of players (int), players per group (int)
    output: player groups (list of lists)
    """
    import random

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

    return group_matrix


"""
data = [
    [
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 2, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 2, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 3, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 3, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        #
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 2, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 2, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 3, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 3, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 1.5, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        #
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 3, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 3, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        #
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 1, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 2, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 2, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 3, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 3, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 4, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 5, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True,
         "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
    ]
]
"""

    ##Random rounds
def shuffle(data):
    #Aleatoriza los grupos donde se encontrarán los jugadores si "shuffle": True
    # random.sample does not shuffle data in place. random.shuffle would work in this case but
    # could lead to bugs if we are say trying to write the data to csv after having used
    # it in the experiment.
    return [random.sample(data[0], k=len(data[0]))]

def export_data():
#    return shuffle(data)
    return data

def export_data_authority():
    """
    Exports the data for a session with authority
    """
    return data_au

def export_data_no_authority():
    """
    Exports the data for a session with NO authority
    """
    return data_nau

# VARIABLES/ATRIBUTOS UTILIZADOS


#EN CLASE PLAYER:

#audit2: Variable auxiliar para aleatorizar la auditoría
#transcribed_text: Transcripción realizada en el modo de Transcripción de Práctica
#transcribed_text2 Transcripción realizada en cada ronda de manera oficial
#levenshtein_distance: Valor de la distancia de levenstein (medida de la precisión de la transcrip.)
#ratio: Porcentaje correcto de la transcripción hecha por el jugador
#contribution: Ingreso reportado por el jugador por ronda
#income: Dotación por ronda recibida por el jugador
#spanish: Variable auxiliar que indica si se está jugando en español o inglés
#done: Variable sin uso (revisar más veces)
#transcriptionDone: Variable auxiliar que indica si se realizó la transcripción correctamente (con un porcentaje
# aceptable)
#payoff: Pago del jugador por ronda

#baseIncome: Variable sin uso (revisar más veces)
#total_report: Variable sin uso (revisar más veces)
#total_contribution: Suma de las contribuciones
#total_earnings: Suma de las ganancias (contribucion total*multiplicador)
#individual_share: Suma de las ganancias entre la cantidad de jugadores
# (contribucion total*multiplicador/número de jugadores)
#temp: Variable que toma como valor la dotación del jugador solo si esta coincide con la dotación reportada
#authority_ID: Id del jugador que fue elegido como la autoridad
#authority_multiply: Variable auxiliar que indica si el jugador decidió multiplicar las contribuciones
#auth_appropriate: Variable auxiliar que indica si el jugador decidió apropiarse o no de
# parte de lo contribuido*multiplicador
#total_reported_income: Variable sin uso (revisar más veces)
#appropriation: Cantidad que la autoridad tomó en caso haya optado por la apropiación
#refText: Texto que debe ser transcrito por el jugador


#EN CLASE GRUPO: