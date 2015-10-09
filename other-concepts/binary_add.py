def binary_add(num1, num2):
	"""
	Given two binary numbers as strings, returns the sum of binary numbers as a string.

	>>> binary_add('111', '10')
	'1001'

	>>> binary_add('10', '1101')
	'1111'
	"""
	i = len(num1) - 1
	j = len(num2) - 1
	carry = 0
	res = ''

	while i >= 0 or j >= 0:
		digit1 = num1[i] if i >= 0 else 0
		digit2 = num2[j] if j >= 0 else 0
		digit_sum = int(digit1) + int(digit2) + carry

		carry = 1 if digit_sum > 1 else 0
		new_digit = 1 if digit_sum % 2 == 1 else 0

		res = str(new_digit) + res

		i -= 1
		j -= 1

	if carry > 0:
		res = '1' + res

	return res

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()