#########################################################################################
# 					Exercise 9.5 of Cracking the Coding Interview v5					#
#																						#
#		Write a method to compute all permutations of a string of unique characters		#
#########################################################################################

def compute_permutations(string):
	"""
	Computes all permutations of a string

	>>> compute_permutations("cat")
	['cat', 'act', 'atc', 'cta', 'tca', 'tac']

	>>> compute_permutations("ab")
	['ab', 'ba']
	"""

	if len(string) == 1:
		return [string]

	permutations = compute_permutations(string[1:])
	first_char = string[0]
	result = []

	for perm in permutations:
		for i in range(len(perm)+1):
			result.append(insert_char_at(perm, first_char, i))
			# can append perm[:i] + first_char + perm[i:] instead of helper function if preferred

	return result

def insert_char_at(word, c, i):
	""" 
	Inserts character to a string at a certain index

	>>> insert_char_at("coffee", "f", 3)
	'cofffee'

	>>> insert_char_at("bcd", "a", 0)
	'abcd'
	"""
	start = word[:i]
	end = word[i:]
	return start + c + end

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()