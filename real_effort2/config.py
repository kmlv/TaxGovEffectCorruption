import random

# Dictionary Format: endowment, multiplier, tax, transcription, authority mode, transcription difficulty, spanish toggle,
##            audit penalty, appropriation percent, shuffle
# Each dictionary entry represents the data values for 1 round
data = [
    [
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 3, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        #
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        #
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},

    ]
]
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
#refText: Texto que debe ser transcrito por el jugador


#EN CLASE GRUPO:

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