"""
A majority element in an array A[] of size n is an element that appears more than n/2 times
(and hence there is at most one such element)

Write a funciton which takes an array and emits the majority element (if it exists),
otherwise returns None
"""

# Time: O(n)
# Space: O(n)
def majority_element(num_list):
	"""
	Given a list, returns the majority element if one exists

	>>> majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4])
	4

	>>> majority_element([3, 3, 4, 2, 4, 4, 2, 4])

	"""
	num_dict = {}

	for num in num_list:
		num_dict[num] = num_dict.get(num, 0) + 1
		if num_dict[num] > len(num_list)/2:
			return num

	return None


#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()