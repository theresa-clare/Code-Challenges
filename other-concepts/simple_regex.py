"""
Given a regular expression pattern and a string, check to see if the pattern matches the string

* --> 0 or more
. --> anything and has to be present
"""

def tokenize(pattern):
	""" 
	Returns a list of the pattern tokenized

	>>> tokenize("c*b*c.")
	['c*', 'b*', 'c', '.']

	>>> tokenize("cc")
	['c', 'c']

	>>> tokenize("")
	[]
	"""
	if pattern is None:
		return None
	elif len(pattern) == 0:
		return []

	res = []
	i = 0

	while i < len(pattern):
		if i+1 < len(pattern) and pattern[i+1] == '*':
			res.append(pattern[i:i+2])
			i += 2
		else:
			res.append(pattern[i])
			i += 1

	return res

def match_tokenized_regex_pattern(pattern, string):
	"""
	Given a tokenized list of a regex pattern and a string, returns True if the 
	pattern matches the string; returns False otherwise

	>>> match_tokenized_regex_pattern(['c*', 'b*', 'c', '.'], "ccbcd")
	True

	>>> match_tokenized_regex_pattern(['c', 'b', '.'], "cbd")
	True

	>>> match_tokenized_regex_pattern(['c', 'c'], "abc")
	False
	"""
	if not pattern and not string: # if reach the end of both pattern and string
		return True
	if not pattern or not string: # if reach the end of either pattern and string
		return False

	p = pattern[0]
	c = string[0]

	# removes cases with (letter-symbol vs. letter) and (non-matching single letters)
	if p == c or p == '.':
		return match_tokenized_regex_pattern(pattern[1:], string[1:])

	# X* --> X can appear 0 times, once, or more (3 cases)
	elif len(pattern) > 1:
		if pattern[0] == c:
			is_match = match_tokenized_regex_pattern(pattern, string[1:]) # appear >= 1 times
			if is_match:
				return True
		return match_tokenized_regex_pattern(pattern[1:], string) # appear 0 times in string

	# non-matching single letters
	else:
		return False

#########################################################################################

def is_char_match(char, pattern_char):
	return char == pattern_char or pattern_char == '.'

def is_match(string, pattern):
	if pattern is None or pattern = '':
		return not bool(subject)

	if len(pattern) > 1 and pattern[1] == '*':
		# return 0 occurrences or (1 occurrence and more occurences)
		return is_match(subject, pattern[2:]) or \
		(is_char_match(subject[0], pattern[0]) and \
		is_match(subject[1:], pattern))
	else: # non-star case
		return is_char_match(subject[0], pattern[0]) and is_match(subject[1:], pattern[1:])

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()