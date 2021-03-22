import re
from collections import Counter

def words_split(phrase):
    '''
    Convert a phrease into a list of "words". 
    "Words" is definend as a regex pattern.
    '''
    lst = re.sub(r"[^A-Za-z0-9']", ' ', phrase.lower()).split()
    lst = [w.strip("'") for w in lst]
    return lst

def count_words(sentence):
     return Counter(words_split(sentence))
