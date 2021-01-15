import re

stop_words = ['the', 'and']

def clean(s):
    s = re.sub(r'[\.!?,]', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s

def removeStopWords(utterance):
    utterance = clean(utterance)
    utterance = utterance.lower()

    for stop_word in stop_words:
        utterance = re.sub(r'^|[\s]?' + stop_word + r'(?![a-z])', ' ', utterance)

    utterance = re.sub(r'\s+', ' ', utterance)
    utterance = utterance.strip()
    return utterance
    
