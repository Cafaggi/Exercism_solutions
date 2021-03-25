import re

def abbreviate(words: 'srt') -> 'str':
    words = re.sub(r"[^a-zA-Z('^a-zA-Z)]+",' ', words).split()
    return "".join([word[0].upper() for word in words])
    