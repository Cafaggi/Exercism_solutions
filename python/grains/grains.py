def square(number):
    if number > 64 or number <= 0: raise ValueError('number must be grater than 0 and smaller or equal than 64')
    return 2**(number-1)


def total():
    return 2**64 -1
