# http://www.geeksforgeeks.org/print-all-combinations-of-given-length/

"""
Print all possible strings of length k that can be formed from a set
of n characters
	--> Given a set of characters and a positive integer k, print all
		possible strings of length k that can be formed from the set
"""

def k_words_from_chars(char_list, k):
	"""
	Prints all k-words from a list of characters

	>>> k_words_from_chars(['a','b'], 3)
	aaa
	aab
	aba
	abb
	baa
	bab
	bba
	bbb

	>>> k_words_from_chars(['a','b','c','d'], 1)
	a
	b
	c
	d
	"""
	print_k_words_from_chars(char_list, "", k)

def print_k_words_from_chars(char_list, prefix, k):
	if k == 0:
		print prefix
		return

	for i in range(len(char_list)):
		new_prefix = prefix + char_list[i]
		print_k_words_from_chars(char_list, new_prefix, k-1)

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()