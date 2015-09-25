"""
Given an unsorted array of non-negative integers, find a continuous subarray
which adds to a given number

# http://www.geeksforgeeks.org/find-subarray-with-given-sum/
"""

# Naive method
# Time: O(n^2)
def subsequence_sum_to_target(num_array, target):
	"""
	Returns contiguous subsequence whose sum equals to target; returns None otherwise

	>>> subsequence_sum_to_target([1, 4, 20, 3, 10, 5], 33)
	[20, 3, 10]

	>>> subsequence_sum_to_target([1, 4, 0, 0, 3, 10, 5], 7)
	[4, 0, 0, 3]

	>>> subsequence_sum_to_target([1, 4], 0)

	"""	
	for i in range(len(num_array)):
		total = 0
		for j in range(i, len(num_array)):
			total += num_array[j]
			if total == target:
				return num_array[i:j+1]
			if total > target:
				break

	return None

#########################################################################################

# Efficient method
# Time: O(n)
def subarray_sum_to_target(num_array, target):
	"""
	Returns contiguous subsequence whose sum equals to target; returns None otherwise

	>>> subarray_sum_to_target([1, 4, 20, 3, 10, 5], 33)
	[20, 3, 10]

	>>> subarray_sum_to_target([1, 4, 0, 0, 3, 10, 5], 7)
	[4, 0, 0, 3]

	>>> subarray_sum_to_target([1, 4], 0)

	"""	
	total = num_array[0]
	start = 0

	for i in range(1, len(num_array)+1):
		# if total exceeds the target, then remove the starting elements
		while total > target and start < i-1:
			total -= num_array[start]
			start += 1
		# if total becomes equal to target, then return subarray
		if total == target:
			return num_array[start:i]
		# add this element to total
		if i < len(num_array):
			total += num_array[i]

	return None

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()