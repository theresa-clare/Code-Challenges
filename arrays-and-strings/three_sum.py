""" 
Given an array of integers and a target sum, find the indices where a[i] + a[j] + a[z] = k
"""

# Time: O(n^2)
# Space: O(n)
def three_sum(int_array, k):
	"""
	Returns a tuple with the indices where a[i] + a[j] + a[z] = k given an array of
	integers and a target sum

	>>> three_sum([10, 3, 2, 5, 0], 5)
	(1, 2, 4)

	>>> three_sum([1, 15, 8, -10, 5], 4)
	(None, None, None)
	"""
	int_dict = {}
	int_set = set(int_array)

	for i, num in enumerate(int_array):
		int_dict.setdefault(num, []).append(i)

	for i in range(len(int_array)):
		for j in range(i+1, len(int_array)):
			difference = int_array[i] + int_array[j]
			if k - difference in int_set:
				return i, j, int_dict[k - difference][0]

	return None, None, None

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()