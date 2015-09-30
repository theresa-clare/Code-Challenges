"""
Cracking the Coding Interview v6: Exercise 17.19

You are given an array with all the numbers from 1 to N appearing exactly once,
except for one number that is missing. How can you find the missing number in 
O(N) time and O(1) space?
"""

def missing_number(num_array):
	"""
	Returns missing number in array

	>>> missing_number([1, 2, 3, 4, 6, 7, 8, 9, 10])
	5

	>>> missing_number([2, 3, 4, 5])
	1

	>>> missing_number([1, 2, 3, 4])
	'No missing numbers'

	>>> missing_number([])

	"""
	if num_array is None or len(num_array)<1:
		return None
	if num_array[0] != 1:
		return 1

	total = sum(range(1, num_array[-1]+1))

	# option over sum function:
	# n = len(num_array)
	# total = ((n+1)*(n+2))/2

	for num in num_array:
		total -= num

	if total == 0:
		return 'No missing numbers'
	return total

"""
Continuation of the problem: What if there were two numbers missing?
"""
def missing_two(num_array):
	# Will come back to complete this function
	pass

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()