""" Given an array of ints, find at least one pair of i,j: a[i] + a[j] == 0 """

def two_sum(num_list):
	"""
	Returns tuple of the first instance where indices where a[i] + a[j] == 0

	>>> two_sum([1,5,2,0,-3,-2])
	(2, 5)

	>>> two_sum([0,2,6,3,0,1,-2])
	(0, 4)

	>>> two_sum([1,2,3,4,5])
	(None, None)
	"""
	num_dict = {}
	zero_count = 0

	for i, num in enumerate(num_list):
		if num == 0:
			zero_count += 1
			if zero_count == 2:
				return num_dict[num], i

		num_dict[num] = i
		
		if -num in num_dict and num != 0:
			return num_dict[-num], i

	return None, None

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()