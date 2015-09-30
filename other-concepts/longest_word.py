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

# Recursively see if can build right side from other elements in array to account for
# composites of more than one word (uses dynamic programming and memoization)

def get_longest_word(words):
	"""
	Returns longest word made of other words in the list

	>>> get_longest_word(["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"])
	'dogwalker'

	>>> get_longest_word(["apple", "berry", "cherry", "appleberrycherry", "durian", "berrycherry"])
	'appleberrycherry'

	>>> get_longest_word(["cat", "dog", "squirrel", "seahorse"])

	>>> get_longest_word([])

	"""
	words.sort(key=len, reverse=True)
	word_dict = {}

	for word in words:
		word_dict[word] = True

	for w in words:
		if can_build_word(w, True, word_dict):
			return w

	return None

def can_build_word(string, is_original, word_dict):
	if string in word_dict and not is_original:
		return True

	for i in range(1, len(string)):
		left = string[:i]
		right = string[i:]

		if left in word_dict and word_dict[left] == True and \
		can_build_word(right, False, word_dict):
			return True

	word_dict[string] = False
	return False

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()