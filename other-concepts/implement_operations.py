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

if __name__ == '__main__':
	import doctest
	doctest.testmod()