""" 
Cracking the Coding Interview v5: Exercise 9.3

A magic index in array A[0 ... n-1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index,
if one exists, in array A.
"""

# Non-recursive, brute force solution
def find_magic_i(A):
	for i in range(len(A)):
		if A[i] == i:
			return True
	return False

# Recursive binary search method
def find_magic_i(A, start, end):
	if end < start or start < 0 or end >= len(A):
		return False

	mid = (start + end)/2

	if A[mid] == mid:
		return mid
	elif A[mid] > mid:
		return find_magic_i(A, start, mid - 1)
	else:
		return find_magic_i(A, mid + 1, end)

def find_magic_i_wrapper(A):
	return find_magic_i(A, 0, len(A) - 1)



""" Follow up: What if the elements are not distinct? """

def find_magic_i_nondistinct(A, start, end):
	if end < start or start < 0 or end >= len(A):
		return False

	mid_i = (start + end)/2
	mid_val = A[mid_i]

	if mid_val == mid_i:
		return mid_i

	left_i = min(mid_i - 1, mid_val)
	left = find_magic_i_nondistinct(A, start, left_i)

	if left >= 0:
		return left

	right_i = max(mid_i + 1, mid_val)
	right = find_magic_i_nondistinct(A, right_i, end)

	return right

def find_magic_i_nondistinct_wrapper(A):
	return find_magic_i_nondistinct(A, 0, len(A) - 1)