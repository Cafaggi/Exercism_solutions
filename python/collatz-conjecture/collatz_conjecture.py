def steps(number):
    if isinstance(number, int) and number>0:
        steps = 0
        residue = number
        while residue != 1:
            if residue%2 == 0:
                residue = residue/2
                steps += 1
            else:
                residue = residue*3+1
                steps += 1
        return steps

    else:
        raise ValueError('this is not an integer number')
