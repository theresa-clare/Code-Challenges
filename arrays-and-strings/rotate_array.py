"""
Rotate an array left by d elements

http://www.geeksforgeeks.org/array-rotation/
"""

def rotate_array(num_list, d):
	"""
	Given a list, rotate the list by d elements

	>>> rotate_array([1,2,3,4,5], 3)
	[4, 5, 1, 2, 3]

	>>> rotate_array([1,2,3], 4)
	[2, 3, 1]

	>>> rotate_array([1,2,3,4,5], -1)
	[5, 1, 2, 3, 4]
	"""
	if d == 0:
		return num_list
	elif d > len(num_list):
		return num_list[d-len(num_list):] + num_list[:d-len(num_list)]
	else:
		return num_list[d:] + num_list[:d]

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()