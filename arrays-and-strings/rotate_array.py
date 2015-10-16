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

def rotate_array_v2(num_list, d):
	"""
	Given a list, rotates the list left by d elements.

	>>> rotate_array_v2([1,2,3,4,5], 3)
	[4, 5, 1, 2, 3]

	>>> rotate_array_v2([1,2,3], 4)
	[2, 3, 1]

	>>> rotate_array_v2([1,2,3,4,5], -1)
	[5, 1, 2, 3, 4]
	"""
	if d == 0:
		return num_list
	elif d > 0:
		for i in range(d):
			# rotate left
			temp = num_list[0]
			for j in range(1, len(num_list)):
				num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
			num_list[-1] = temp
	else: # d < 0
		for i in range(abs(d)):
			# rotate right
			temp = num_list[-1]
			for j in reversed(range(len(num_list)-1)):
				num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
			num_list[0] = temp
	return num_list

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()