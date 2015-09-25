"""
Find the median of a rotated sorted list
"""

def find_pivot(num_list, low, high):
	"""
	Returns the index of the pivot point of the rotated sorted array

	>>> find_pivot([3, 4, 5, 6, 1, 2], 0, 5)
	3

	>>> find_pivot([1, 2, 3, 4, 5], 0, 4)
	-1

	"""
	if high < low:
		return -1
	if high == low:
		return low

	mid = (low + high)/2

	if mid < high and num_list[mid] > num_list[mid+1]:
		return mid
	if mid > low and num_list[mid] < num_list[mid-1]:
		return mid -1

	if num_list[low] >= num_list[mid]:
		return find_pivot(num_list, low, mid-1)
	else:
		return find_pivot(num_list, mid+1, high)

def find_median(num_list):
	"""
	Returns the median in a rotated sorted array

	>>> find_median([3, 4, 5, 6, 1, 2])
	3.5

	>>> find_median([3, 4, 5, 1, 2])
	3

	>>> find_median([1, 2, 3, 4, 5, 6])
	3.5

	>>> find_median([1, 2, 3, 4, 5])
	3
	"""
	pivot = find_pivot(num_list, 0, len(num_list)-1)
	sorted_array = []

	if pivot == -1:
		sorted_array = num_list
	else:
		sorted_array = num_list[pivot+1:] + num_list[:pivot+1]

	mid = len(sorted_array)/2

	if len(sorted_array)%2 == 0:
		return float((sorted_array[mid-1] + sorted_array[mid]))/2
	else:
		return sorted_array[mid]

#########################################################################################

def find_median_optimized(num_list):
	"""
	Returns the median in a rotated sorted array

	>>> find_median_optimized([3, 4, 5, 6, 1, 2])
	3.5

	>>> find_median_optimized([3, 4, 5, 1, 2])
	3

	>>> find_median_optimized([1, 2, 3, 4, 5, 6])
	3.5

	>>> find_median_optimized([1, 2, 3, 4, 5])
	3
	"""
	pivot = find_pivot(num_list, 0, len(num_list)-1)
	mid = len(num_list)/2
	new_mid = (mid + pivot + 1) % len(num_list)

	if len(num_list)%2 == 1:
		if pivot == -1:
			return num_list[mid]
		else:
			return num_list[new_mid]
	else:
		if new_mid == len(num_list)-1:
			return float(num_list[0] + num_list[new_mid])/2
		else:
			return float(num_list[new_mid-1] + num_list[new_mid])/2

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()