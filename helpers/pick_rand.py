from random import randint

def pick_rand(dictionary, n):
    picked = {}

    while len(picked) < n:
        index = randint(0, len(dictionary) - 1)
        if index not in picked.keys():
            picked[index] = dictionary[str(index)]
    
    return picked
