import re

def clean(text):
    cleaned = re.sub(r'[!?\.,-]+', ' ', text)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = cleaned.lower()

    return cleaned

def countWords(text):
    words_count = {}

    text = clean(text)
    for token in text.split():
        if token not in words_count:
            words_count[token] = 0
        
        words_count[token] += 1

    sorted_words_count = {word:words_count[word] for word in sorted(words_count)}
    return sorted_words_count
    