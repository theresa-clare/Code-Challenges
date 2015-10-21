""" Given an array of ints, find all pairs where a[i] + a[j] == 0 """

def two_sum_all(int_array):
	"""
	Returns list of tuples of indices where a[i] + a[j] == 0 given an array of ints

	>>> two_sum_all([1,4,9,-4,2,-1])
	[(1, 3), (0, 5)]

	>>> two_sum_all([8,3,5,0,1,2,0])
	[(3, 6)]

	>>> two_sum_all([0,0,0])
	[(0, 1), (1, 2), (0, 2)]
	"""
	int_dict = {}
	ij_pairs = set()

	for i, num1 in enumerate(int_array):
		for j, num2 in enumerate(int_array):
			if i !=j and num1 + num2 == 0 and (j,i) not in ij_pairs:
				ij_pairs.add((i,j))

	return list(ij_pairs)

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()