"""
K'th smallest/largest element in unsorted array
	--> Given an array and a number k where k is smaller than the size of
	the array, we need to find the k'th smallest/largest element in the
	given array. It is given that all array elements are distinct

http://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
"""

# Naive solution
# Time: O(n log(n))
# Space: O(n)
def kth_smallest(num_list, k):
	"""
	Returns kth largest element in array

	>>> kth_smallest([12, 3, 5, 7, 1, 10, 19], 3)
	5

	>>> kth_smallest([10, 9, 4, 7, -1], 2)
	4

	>>> kth_smallest([], 2)

	"""
	if num_list is None or k is None:
		return None

	if k > len(num_list):
		return None

	sorted_num_list = sorted(num_list)

	# if looking for kth largest, return sorted_num_list[-k]
	return sorted_num_list[k-1]


#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()