def is_pangram(sentence):
    dir={}
    suma=0
    for letter in sentence.lower():
        if letter.isalpha():
            dir.setdefault(letter,1)
    suma=len(dir.values())
    if suma==26:
        return True
    else:
        return False
    
    
    
        
