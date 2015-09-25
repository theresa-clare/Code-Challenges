#########################################################################################
# 					Exercise 1.5 of Cracking the Coding Interview v5					#
#																						#
# Implement a method to perform basic string compression using the counts of repeated	#
# characters. 																			#
# 		Input: "aabcccccaaa"															#
# 		Output: "a2b1c5a3"																#
# If the "compressed" string would not become smaller than the original string, your 	#
# method should return the original string. You can assume the string has only upper 	#
# and lowercase letters (a-z). 															#
#########################################################################################

# Time: O(n)

def compress(string):
	"""
	>>> compress("aabcccccaaa")
	'a2b1c5a3'

	>>> compress("aabbba")
	'a2b3a1'

	>>> compress("abcdefg")
	'abcdefg'
	"""

	past_chars = [string[0]]
	char_counts = [1]

	for i in range(1, len(string)):
		if string[i] == past_chars[-1]:
			char_counts[-1] += 1
		else:
			past_chars.append(string[i])
			char_counts.append(1)

	compressed_string = ""

	for char, count in zip(past_chars, char_counts):
		compressed_string += char + str(count)

	if len(compressed_string) > len(string):
		return string

	return compressed_string


#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()