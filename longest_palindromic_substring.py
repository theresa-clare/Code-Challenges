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
	>>> dynamic_LPS("forgeeksskeegfor")
	'geeksskeeg'

	>>> dynamic_LPS("l")
	'l'

	>>> dynamic_LPS("no palindrome")
	''
	"""

	if len(string) == 1:
		return string

	max_start = 0
	max_end = 0

	for i in range(1, len(string)):
		start = i - 1
		end = i + 1

		while start >= 0 and end < len(string):
			if string[start] == string[end]:
				start -= 1
				end += 1
			else:
				start += 1
				end -= 1
				break

		if end - start > max_end - max_start:
			max_start = start
			max_end = end

		start = i-1
		end = i

		while start >= 0 and end < len(string):
			if string[start] == string[end]:
				start -= 1
				end += 1
			else:
				start += 1
				end -= 1
				break

		if end - start > max_end - max_start:
			max_start = start
			max_end = end

	if max_end-1-max_start > 1:
		return string[max_start:max_end+1]
	else:
		return ""

#########################################################################################

# for substring without repetition	
def nonrepetitive_dynamic_LPS(string):
	"""
	>>> nonrepetitive_dynamic_LPS("forgeeksskeegfor")
	'geeksskeeg'

	>>> nonrepetitive_dynamic_LPS("l")
	'l'

	>>> nonrepetitive_dynamic_LPS("no palindrome")
	''
	"""
	if len(string) == 1:
		return string

	max_start = 0
	max_end = 0

	for i in range(1,len(string)):
		for j in range(2):	
			start = i-1
			end = i+j
			while start >= 0 and end < len(string):
				if string[start] == string[end]:
					start -= 1
					end += 1
				else:
					start += 1
					end -= 1
					break

			if end-start > max_end-max_start:
				max_start = start
				max_end = end

	if max_end-1-max_start > 1:
		return string[max_start:max_end+1]
	else:
		return ""

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()