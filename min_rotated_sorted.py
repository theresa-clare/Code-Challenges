"""
Find the minimum element in a sorted and rotated array

http://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/
"""

# Time: O(n)
# Space: O(1)
def naive_min_rotated_sorted(num_list):
	"""
	Given a rotated, sorted array, finds the minimum element

	>>> naive_min_rotated_sorted([5, 6, 1, 2, 3, 4])
	1

	>>> naive_min_rotated_sorted([1, 2, 3, 4])
	1

	>>> naive_min_rotated_sorted([2, 1])
	1
	"""
	if num_list is None:
		return None
	elif len(num_list) == 1:
		return num_list[0]
	elif num_list[0] < num_list[-1]:
		return num_list[0]
	else:
		for i in range(len(num_list)-1):
			if num_list[i] > num_list[i+1]:
				return num_list[i+1]

#########################################################################################

# Note: Assumes elements are unique!
# Time: O(log(n)) using binary search
# Space: O(1)
def min_rotated_sorted(num_list, low, high):
	if high < low:
		return num_list[0]
	elif high == low:
		return num_list[low]

	mid = (low + high)/2

	# Check if element at mid+1 is the minimum
	if mid < high and num_list[mid] > num_list[mid+1]:
		return num_list[mid+1]
	# Check if element at mid is the minimum
	elif mid > low and num_list[mid] < num_list[mid-1]:
		return num_list[mid]

	elif num_list[high] > num_list[mid]:
		return min_rotated_sorted(num_list, low, mid-1)
	else:
		return min_rotated_sorted(num_list, mid+1, high)

def min_rotated_sorted_wrapper(num_list):
	"""
	Given a rotated, sorted array, finds the minimum element

	>>> min_rotated_sorted_wrapper([5, 6, 1, 2, 3, 4])
	1

	>>> min_rotated_sorted_wrapper([1, 2, 3, 4])
	1

	>>> min_rotated_sorted_wrapper([2, 1])
	1
	"""
	return min_rotated_sorted(num_list, 0, len(num_list)-1)

#########################################################################################

# Note: Time increases if there are non-unique elements
# Time: O(n)
# Space: O(1)
def min_rotated_sorted_nonunique(num_list, low, high):
	if high < low:
		return num_list[0]
	elif high == low:
		return num_list[low]

	mid = (low + high)/2

	# Check if element at mid+1 is the minimum
	if mid < high and num_list[mid] > num_list[mid+1]:
		return num_list[mid+1]
	# Check if element at mid is the minimum
	elif mid > low and num_list[mid] < num_list[mid-1]:
		return num_list[mid]

	# Causes O(n) time; need to check both sides with duplicates
	if num_list[low] == num_list[mid] and num_list[mid] == num_list[high]:
		return min(min_rotated_sorted_nonunique(num_list, low, mid-1), \
					min_rotated_sorted_nonunique(num_list, mid+1, high))

	elif num_list[high] > num_list[mid]:
		return min_rotated_sorted(num_list, low, mid-1)
	else:
		return min_rotated_sorted(num_list, mid+1, high)

def min_rs_nonunique_wrapper(num_list):
	"""
	Given a rotated, sorted array, finds the minimum element

	>>> min_rs_nonunique_wrapper([2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2])
	0

	>>> min_rs_nonunique_wrapper([5, 6, 1, 2, 3, 4])
	1

	>>> min_rs_nonunique_wrapper([1, 2, 3, 4])
	1

	>>> min_rs_nonunique_wrapper([2, 1])
	1
	"""
	return min_rotated_sorted_nonunique(num_list, 0, len(num_list)-1)


#########################################################################################


if __name__ == "__main__":
	import doctest
	doctest.testmod()
