def is_armstrong_number(number):
    Num_str=str(number)
    Number_of_digits=len(Num_str)
    Total=0
    for digit in Num_str:
        Total+=int(digit)**(Number_of_digits)
    return Total==number
    
        
    
