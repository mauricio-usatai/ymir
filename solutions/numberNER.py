import re

numbers = {
    'one': 1,
    'two': 2,
    'three': 3
}

def clean(s):
    print(s)
    s = re.sub(r'[,.]', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s

def numberNER(utterance):
    entity_values = []

    utterance = clean(utterance)
    
    for token in utterance.split(' '):
        if token in numbers:
            entity_values.append(numbers[token])
    
    return entity_values