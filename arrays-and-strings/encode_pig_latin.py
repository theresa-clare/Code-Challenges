"""
Given a string, return the pig latin translation

constant first: 	hello --> ello-hay
vowel first: 		egg --> egg-yay
y first: 			yellow --> ellow-yay
y second:			my --> y-may
y after cluster:	rhythm --> ythm-rhay
"""

def encode_pl_word(word):
	"""
	Given a word, returns the pig latin translation of the word

	>>> encode_pl_word("hello")
	'ello-hay'

	>>> encode_pl_word("egg")
	'egg-yay'

	>>> encode_pl_word("yellow")
	'ellow-yay'

	>>> encode_pl_word("my")
	'y-may'

	>>> encode_pl_word("rhythm")
	'ythm-rhay'
	"""
	vowels = {'a', 'e', 'i', 'o', 'u'}

	if not word:
		return None

	if word[0] in vowels:
		return word + '-' + 'yay'
	elif word[0] == 'y':
		return word[1:] + '-' + word[0] + 'ay'
	elif word[1] == 'y':
		return word[1] + '-' + word[0] + 'ay'
	else:
		beginning = ""
		for i, char in enumerate(word):
			if char not in vowels and char != 'y':
				beginning += char
			else:
				return word[i:] + '-' + beginning + 'ay'

def encode_pl_string(string):
	"""
	Given a string, returns string translated to pig latin

	>>> encode_pl_string("hello egg my yellow rhythm")
	'ello-hay egg-yay y-may ellow-yay ythm-rhay'

	>>> encode_pl_string("")
	''
	"""
	word_list = string.split()
	pl_word_list = []

	for word in word_list:
		pl_word_list.append(encode_pl_word(word))

	return " ".join(pl_word_list)

#########################################################################################


if __name__ == "__main__":
	import doctest
	doctest.testmod()