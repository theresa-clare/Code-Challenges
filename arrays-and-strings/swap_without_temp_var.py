"""
Cracking the Coding Interview v6: Exercise 16.1

Write a function to swap a number in place (that is, without temporary variables)
"""

def swap_without_temp_var(num_array, i, j):
	"""
	Given an array and two indices, swap the numbers at the indices without a temp variable

	>>> swap_without_temp_var([1,2,3,4,5], 0, 3)
	[4, 2, 3, 1, 5]

	>>> swap_without_temp_var([5,4,3,2,1], 1, 4)
	[5, 1, 3, 2, 4]

	>>> swap_without_temp_var([4,3,2,6,3], 5, 2)

	"""

	if num_array is None or i > len(num_array)-1 or j > len(num_array)-1:
		return None

	bigger = i if max(num_array[i], num_array[j]) == num_array[i] else j
	smaller = i if min(num_array[i], num_array[j]) == num_array[i] else j

	num_array[bigger] -= num_array[smaller]
	num_array[smaller] += num_array[bigger]
	num_array[bigger] = num_array[smaller] - num_array[bigger]

	return num_array


#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()