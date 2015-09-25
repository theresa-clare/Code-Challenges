#################################################################################
# 				Exercise 1.1 of Cracking the Coding Interview v5				#
#																				#
#	Implement an algorithm to determine if a string has all unique characters	#
#################################################################################

# Time:	O(n)
# Space: O(n)
def all_unique(string):
	""" 
	>>> all_unique("hello world")
	False

	>>> all_unique("python")
	True
	"""

	unique_chars = set()

	for char in string:
		if char in unique_chars:
			return False
		unique_chars.add(char)
	return True

#################################################################################
#        Continuation of Exercise 1.1 of Cracking the Coding Interview v5		#
#																				#
#				What if you cannot use additional data structures?				#
#################################################################################

# Time: O(n log(n))
# Space: O(n)
def all_unique_v2(string):
	"""
	>>> all_unique_v2("chocolate")
	False

	>>> all_unique_v2("machine")
	True
	"""
	sorted_string = sorted(string)
	for i in range(len(string)-1):
		if sorted_string[i] == sorted_string[i+1]:
			return False
	return True

# Time: O(n^2)
# Space: O(1)
def all_unique_v3(string):
	"""
	>>> all_unique_v3("vanilla")
	False

	>>> all_unique_v3("light")
	True
	"""

	for i, char in enumerate(string):
		for j, other_char in enumerate(string):
			if char == other_char and i != j:
				return False
	return True

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()