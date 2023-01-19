from collections import Counter
from string import punctuation

def load_text(input_file):
    '''load text from a file and display as a string'''
    with open(input_file, "r") as file:
        text = file.read()
    return text 

def clean_text(text):
    '''lowercase and remove punctuations from text'''
    text = text.lower()
    for p in punctuation:
        text = text.replace(p,"")
    return text

def words_counter(input_file):
    '''count unique words in text'''
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)
