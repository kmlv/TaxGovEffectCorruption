
import math
from random import *
import random
import string


def generateText(difficulty):
    #choose difficulty 1 to 3
    min_char = 4 * difficulty
    max_char = min_char + 6
    allchar = string.ascii_lowercase + string.digits + string.punctuation
    vowels = ('a','e', 'i','o','u')
    
        
    generated = ''

    
    if(difficulty == 1):
        allchar = string.ascii_lowercase
    if(difficulty == 2):
        allchar = string.ascii_lowercase + string.digits
    for i in range(10):
        for i in range(5):
             allchar += vowels[i]

        
    
    
    while(len(generated) < 70 - max_char):
        add = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
        generated += (add + " ")

    return generated

print(generateText(1))