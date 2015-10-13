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

def multiply(a, b):
	"""
	Given two numbers, returns the product using oly the add operator

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

if __name__ == '__main__':
	import doctest
	doctest.testmod()