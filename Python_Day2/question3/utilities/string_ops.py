import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def count_vowels(text):
    return sum(1 for char in text.lower() if char in 'aeiou')
