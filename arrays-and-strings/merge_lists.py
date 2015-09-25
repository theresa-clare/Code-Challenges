#########################################################################################
# 					Exercise 11.1 of Cracking the Coding Interview v5					#
#																						#
#			Given two sorted arrays, A and B, merge A and B in sorted order				#
#########################################################################################

def merge_lists(A, B):
	"""
	Merge two sorted lists in sorted order

	>>> merge_lists([1,2,5,9], [2,3,4,7,8,10])
	[1, 2, 2, 3, 4, 5, 7, 8, 9, 10]

	>>> merge_lists([1,2], [1])
	[1, 1, 2]
	"""

	merged = []
	i = 0
	j = 0

	while i < len(A) and j < len(B):
		if A[i] == B[j]:
			merged.append(A[i])
			merged.append(B[j])
			i += 1
			j += 1
		elif A[i] > B[j]:
			merged.append(B[j])
			j += 1
		else:
			merged.append(A[i])
			i += 1

	if i >= len(A):
		merged.extend(B[j:])
	else:
		merged.extend(A[i:])

	return merged

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()