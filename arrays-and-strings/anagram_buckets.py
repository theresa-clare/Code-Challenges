# Time: O(n * n log n)
# Space: O(n)
def anagram_buckets(words):
	"""
	Given an array of words, print all anagrams together

	>>> anagram_buckets(['cat', 'atc', 'banana', 'cool', 'loco'])
	[['banana'], ['cool', 'loco'], ['cat', 'atc']]

	>>> anagram_buckets(['python', 'thopny', 'ythonp'])
	[['python', 'thopny', 'ythonp']]
	"""
	word_dict = {}

	for word in words:
		sorted_word = "".join(sorted(word))
		if sorted_word in word_dict:
			word_dict[sorted_word].append(word)
		else:
			word_dict[sorted_word] = [word]

	res = []

	for sorted_w, w in word_dict.iteritems():
		res.append(w)

	return res

#########################################################################################

def anagram_buckets_v2(words):
	"""
	Given an array of words, print all anagrams together

	>>> anagram_buckets_v2(['cat', 'atc', 'banana', 'cool', 'loco'])
	[['banana'], ['cool', 'loco'], ['cat', 'atc']]

	>>> anagram_buckets_v2(['python', 'thopny', 'ythonp'])
	[['python', 'thopny', 'ythonp']]
	"""
	word_dict = {"".join(sorted(word)): [] for word in words}

	for w in words:
		word_dict["".join(sorted(w))].append(w)

	return word_dict.values()

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()