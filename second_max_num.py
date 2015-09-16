def second_max_num(num_array):
	""" 
	Returns the second maximum number in the ray; returns None otherwise

	>>> second_max_num([10, 4, -1, 7])
	7

	>>> second_max_num([-5, -2, 0])
	-2

	>>> second_max_num([1])
	"""

	if len(num_array) < 2:
		return None

	max_num = num_array[0]
	second_max = min(num_array)

	for num in num_array:
		if num > max_num:
			second_max = max_num
			max_num = num
		elif num > second_max and num != max_num:
			second_max = num

	return second_max

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()