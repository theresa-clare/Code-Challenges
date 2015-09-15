#########################################################################################
# 					Exercise 1.3 of Cracking the Coding Interview v5					#
#																						#
#	Given two strings, write a method to decide if one is a permutation of the other	#								#
#########################################################################################

# Time: O(n log(n))
# Space: O(n)
def is_permutation(string1, string2):
	"""
	>>> is_permutation("abcd", "dbca")
	True

	>>> is_permutation("abcd", "efgh")
	False
	"""
	sorted_string1 = sorted(string1)
	sorted_string2 = sorted(string2)

	for i in range(len(string1)):
		if sorted_string1[i] != sorted_string2[i]:
			return False

	return True

#########################################################################################

# helper function for next v2 and v3 of is_permutation
def str_count_dict(string):
	"""
	>>> str_count_dict("bubble") == {'b':3, 'u':1, 'l':1, 'e':1}
	True
	"""
	dictionary = {}

	for char in string:
		dictionary[char] = dictionary.get(char,0) + 1

	return dictionary

#########################################################################################

# Time: O(n)
# Space: O(n)
def is_permutation_v2(string1, string2):
	"""
	>>> is_permutation_v2("spoon","onops")
	True

	>>> is_permutation_v2("spoon", "forks")
	False
	"""
	string1_dict = str_count_dict(string1)
	string2_dict = str_count_dict(string2)

	if string1_dict == string2_dict:
		return True
	return False

# Time: O(n)
# Space: O(n)
def is_permutation_v3(string1, string2):
	"""
	>>> is_permutation_v3("cups", "psuc")
	True

	>>> is_permutation_v3("mug", "pug")
	False
	"""

	string1_dict = str_count_dict(string1)

	for c in string2:
		if c in string1_dict:
			string1_dict[c] -= 1
		else:
			return False

	for char, count in string1_dict.iteritems():
		if count != 0:
			return False

	return True


#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()