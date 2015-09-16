def quicksort(num_list):
	"""
	Sorts list of numbers using pivot point

	>>> quicksort([8,1,4,-1])
	[-1, 1, 4, 8]

	>>> quicksort([1,1,1,-4,10])
	[-4, 1, 1, 1, 10]

	>>> quicksort([1])
	[1]
	"""

	if len(num_list) <= 1:
		return num_list

	pivot = num_list[0]
	less = quicksort([x for x in num_list[1:] if x < pivot])
	greater = quicksort([x for x in num_list[1:] if x >= pivot])

	return less + [pivot] + greater
	
#########################################################################################


if __name__ == "__main__":
	import doctest
	doctest.testmod()