def classify(number):
    if number <= 0:
        raise ValueError('the number must be natural')

    aliquote_sum = sum([factor for factor in range(1, number) if number%factor == 0])

    if aliquote_sum > number:
        return 'abundant'
    elif aliquote_sum == number:
        return 'perfect'
    else :
        return 'deficient'

