def factors(value: int):

	factor, prime_number = (list(), 2)
	
	if value < 1:
		raise ValueError('value must be greater than 1')

	while value >= prime_number:
		if value%prime_number == 0:
			factor.append(prime_number)
			value = value/prime_number
		else:
			prime_number += 1

	return factor