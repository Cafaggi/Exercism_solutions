def commands(number):

    secret_hands = list()
    actions = ('wink','double blink','close your eyes','jump')
    binary = bin(number).replace("0b", "")
    length = len(binary)

    for position in range(1,length+1):
        
        if position>=5: secret_hands= secret_hands[::-1]
        if int(binary[length-position])==1 & (position<5):
            secret_hands.append(actions[position-1])
        
    return secret_hands
