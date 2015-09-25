"""
A majority element in an array A[] of size n is an element that appears more than n/2 times
(and hence there is at most one such element)

Write a funciton which takes an array and emits the majority element (if it exists),
otherwise returns None

http://www.geeksforgeeks.org/majority-element/
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

# Using Moore's Voting Algorithm
# Overall Time: O(n)
# Overall Space: O(1)

def find_candidate(num_list):
	"""
	Given a list, returns an element occuring most of the time in the array

	>>> find_candidate([2, 2, 3, 5, 2, 2, 6])
	2

	>>> find_candidate([])

	"""

	if num_list is None or len(num_list) == 0:
		return None

	majority_index = 0
	count = 1

	for i in range(1, len(num_list)):
		if num_list[majority_index] == num_list[i]:
			count += 1
		else:
			count -= 1

		if count == 0:
			majority_index = i
			count = 1

	return num_list[majority_index]

def is_majority(num_list, candidate):
	"""
	Given a list and a candidate, returns True if candidate is the majority element;
	returns False otherwise

	>>> is_majority([1, 1, 1, 7, 2, 1], 1)
	True

	>>> is_majority([1, 1, 1, 7, 2, 2], 1)
	False
	"""
	count = 0

	for num in num_list:
		if num == candidate:
			count += 1

	return count > len(num_list)/2

def find_majority_element(num_list):
	"""
	Given a list, returns the majority element if one exists

	>>> find_majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4])
	4

	>>> find_majority_element([3, 3, 4, 2, 4, 4, 2, 4])

	"""
	candidate = find_candidate(num_list)

	if is_majority(num_list, candidate):
		return candidate
	return None

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()