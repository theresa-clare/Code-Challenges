"""
Given a pig latin string, return normal translation

Note: install pyenchant
"""

import enchant
d = enchant.Dict("en_US")

def decode_pl_word(word):
	"""
	Given a pig latin word, returns the normal translation

	>>> decode_pl_word("ello-hay")
	'hello'

	>>> decode_pl_word("egg-yay")
	'egg'

	>>> decode_pl_word("ellow-yay")
	'yellow'

	>>> decode_pl_word("y-may")
	'my'

	>>> decode_pl_word("ythm-rhay")
	'rhythm'
	"""
	vowels = {'a', 'e', 'i', 'o', 'u'}
	syllable_list = word.split('-')

	if syllable_list[1][0] == 'y' and syllable_list[0][0] in vowels \
	and d.check(syllable_list[0]):
		return syllable_list[0]
	else:
		beginning = syllable_list[1][:-2]
		return beginning + syllable_list[0]

def decode_pl_string(string):
	"""
	Given a string of pig latin words, return the normal translation

	>>> decode_pl_string("ello-hay egg-yay ellow-yay y-may ythm-rhay")
	'hello egg yellow my rhythm'
	"""
	pl_word_list = string.split()
	word_list = []

	for word in pl_word_list:
		word_list.append(decode_pl_word(word))

	return " ".join(word_list)

#########################################################################################


if __name__ == "__main__":
	import doctest
	doctest.testmod()