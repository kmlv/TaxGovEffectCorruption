import random

# Dictionary Format: endowment, multiplier, tax, transcription, authority mode, transcription difficulty, spanish toggle,
#                    audit penalty, appropriation percent, shuffle
# Each dictionary entry represents the data values for 1 round
data = [
    [ 
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": True},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 1, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": True},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 1, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": True},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 3, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 4, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 5, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.3, "transcription": True, "mode": 2, "difficulty": 6, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": False},
        {"end": 100, "multiplier": 2, "tax": 0.5, "transcription": True, "mode": 2, "difficulty": 2, "spanish": True, "penalty": 0.9, "appropriation_percent": 0.25, "shuffle": True},
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
    # random.sample does not shuffle data in place. random.shuffle would work in this case but
    # could lead to bugs if we are say trying to write the data to csv after having used
    # it in the experiment.
    return [random.sample(data[0], k=len(data[0]))]

def export_data():
    return shuffle(data)
