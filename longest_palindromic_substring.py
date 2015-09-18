"""
Longest palindromic substring
	--> Given a string, find the longest substring which is a palindrome
"""

# Brute force solution
# Time: O(n^3)
from is_palindrome import is_palindrome

def longest_palindromic_substring(string):
	"""
	>>> longest_palindromic_substring("forgeeksskeegfor")
	'geeksskeeg'

	>>> longest_palindromic_substring("l")
	'l'

	>>> longest_palindromic_substring("no palindrome")
	''
	"""

	if len(string) == 1:
		return string

	max_palindrome = ""
	max_length = 0

	for i in range(len(string)):
		for j in range(i+1, len(string)):
			if is_palindrome(string[i:j+1]) and j-i > max_length and j+1-i != 1:
				max_palindrome = string[i:j+1]
				max_length = j+1-i

	return max_palindrome

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()