def alternate_pos_neg(num_list):
	"""
	Given a list of numbers, returns a list with alternating positive and negative
	numbers while maintaining order. If there are more positive numbers than negative 
	numbers, they appear at the end of the array, and vice versa.

	>>> alternate_pos_neg([1, 2, 3, -4, -1, 4])
	[1, -4, 2, -1, 3, 4]

	>>> alternate_pos_neg([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])
	[5, -5, 2, -2, 4, -8, 7, 1, 8, 0]

	>>> alternate_pos_neg([-1, -2, 3, -4])
	[3, -1, -2, -4]
	"""
	pos = []
	neg = []
	res = []

	for num in num_list:
		if num < 0:
			neg.append(num)
		else:
			pos.append(num)

	i = 0
	j = 0

	while i < len(pos) or j < len(neg):
		if i < len(pos):
			res.append(pos[i])
		if j < len(neg):
			res.append(neg[j])
		i += 1
		j += 1

	return res

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()