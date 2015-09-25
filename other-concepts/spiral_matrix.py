def top_right_matrix(matrix, nums=[]):
	"""
	Returns matrix without top and right side and the numbers from those sides

	>>> matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
	>>> top_right_matrix(matrix)
	([[5, 6, 7], [9, 10, 11]], [1, 2, 3, 4, 8, 12])
	"""
	if is_empty_matrix(matrix):
		return matrix, nums

	nums += matrix[0]
	new_matrix = []

	for i in range(1, len(matrix)):
		new_matrix.append(matrix[i][:-1])
		nums.append(matrix[i][-1])

	return new_matrix, nums

def bottom_left_matrix(matrix, nums=[]):
	"""
	Returns matrix without bottom and left side and the numbers from those sides

	>>> matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
	>>> bottom_left_matrix(matrix)
	([[2, 3, 4], [6, 7, 8]], [12, 11, 10, 9, 5, 1])
	"""
	if is_empty_matrix(matrix):
		return matrix, nums

	nums += matrix[-1][::-1]
	new_matrix = []

	for i in range(len(matrix)-1)[::-1]:
		new_matrix.insert(0, matrix[i][1:])
		nums.append(matrix[i][0])

	return new_matrix, nums

def is_empty_matrix(matrix):
	"""
	Returns False if matrix is list of empty lists; returns True otherwise

	>>> is_empty_matrix([[], [], []])
	True

	>>> is_empty_matrix([[1], [10, 15]])
	False
	"""
	return matrix == [] or not all(li != [] for li in matrix)

def get_spiral_matrix(matrix, nums=[]):
	"""
	Returns numbers of matrix in a spiral

	>>> matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
	>>> get_spiral_matrix(matrix)
	[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
	"""
	if matrix is None:
		return []

	while not is_empty_matrix(matrix):
		matrix, nums = top_right_matrix(matrix, nums)
		if not is_empty_matrix(matrix):
			matrix, nums = bottom_left_matrix(matrix, nums)

	return nums

def print_spiral_matrix(num_list):
	"""
	Prints elements in array

	>>> print_spiral_matrix([1, 2, 3, 4])
	1 2 3 4

	>>> print_spiral_matrix([1])
	1
	"""
	if num_list is None:
		return None

	for num in num_list:
		print num,

def spiral_matrix(matrix):
	print_spiral_matrix(get_spiral_matrix(matrix))


#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()