"""
Longest palindromic substring
	--> Given a string, find the longest substring which is a palindrome

http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
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

# Dynamic programming solution
# Time: O(n^2)
def dynamic_LPS(string):
	"""
	>>> longest_palindromic_substring("forgeeksskeegfor")
	'geeksskeeg'

	>>> longest_palindromic_substring("l")
	'l'

	>>> longest_palindromic_substring("no palindrome")
	''
	"""

	max_length = 1

	start = 0

	low = 0
	high = 0

	for i in range(1, len(string)):
		low = i - 1
		high = i

		while low >= 0 and high < len(string) and string[low] == string[high]:
			if high-low+1 > max_length:
				start = low
				max_length = high - low + 1
			low -= 1
			high += 1

		low = i-1
		high = i + 1

		while low >= 0 and high < len(string) and string[low] == string[high]:
			if high-low+1 > max_length:
				start = low
				max_length = high - low + 1
			low -= 1
			high += 1

	print string[low:high+1]

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()