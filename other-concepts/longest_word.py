"""
Cracking the Coding Interview v6: Exercise 17.15

Given a list of words, write a program to find the longest word made of other
words in the list

Input: cat, banana, dog, nana, walk, walker, dogwalker
Output: dogwalker
"""

# Only accounts for composites of two words
def longest_word(words):
	"""
	Returns longest word made of other words in the list

	>>> longest_word(["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"])
	'dogwalker'

	>>> longest_word(["cat", "dog", "squirrel", "seahorse"])

	>>> longest_word([])

	"""
	words.sort(key=len, reverse=True)
	word_set = set(words)

	for w in words:
		for i in range(1, len(words)):
			left = w[:i]
			right = w[i:]
			if left in word_set and right in word_set:
				return w

	return None

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()