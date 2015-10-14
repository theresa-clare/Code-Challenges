"""
Cracking the Coding Interview v5: Exercise 7.4

Write methods to implement the multiply, subtract, and divide operations for 
integers. Use only the add operator.
"""

def subtract(a, b):
	"""
	Given two numbers, returns the difference using only the add operator

	>>> subtract(10, 5)
	5

	>>> subtract(0, 5)
	-5
	"""
	return a + -b

#########################################################################################

def multiply(a, b):
	"""
	Given two numbers, returns the product using only the add operator

	>>> multiply(-1, 2)
	-2

	>>> multiply(5, 3)
	15

	>>> multiply(5, 0)
	0
	"""
	if a < b:
		return multiply(b, a)

	product = 0

	for i in range(abs(b)):
		product += a

	if b < 0:
		product = -product

	return product

#########################################################################################

def divide(a, b): # a = bx
	"""
	Given two numbers, returns the quotient using only the add operator.

	>>> divide(10, 5)
	2

	>>> divide(3, 0)
	'Error. Cannot divide by 0'
	"""
	if b == 0:
		return 'Error. Cannot divide by 0'

	abs_a = abs(a)
	abs_b = abs(b)
	product = 0
	quotient = 0

	while product + abs_b <= abs_a:
		product += abs_b
		quotient += 1

	if (a < 0 and b < 0) or (a > 0 and b > 0):
		return quotient
	else:
		return -quotient
	

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()