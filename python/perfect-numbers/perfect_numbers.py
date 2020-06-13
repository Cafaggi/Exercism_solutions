def classify(number):
    try:
        ran=range(number-1,1)
        tot=0
        for i in ran:
            if number % i==0:
                tot+=i
        if tot == number:
            return 'perfect'
        elif tot < number:
            return 'deficient'
        elif tot > number:
            return 'abundant'
        
    except ValueError as e:
        return str(e)
    
