# Time: O(n)
# Space: O(1)
def is_palindrome(word):
	"""
	Returns False if word is not a palindrome; returns True otherwise

	>>> is_palindrome("gatcctag")
	True

	>>> is_palindrome("cheese")
	False
	"""
	if word is None:
		return None

	for i in range(len(word)/2):
		if word[i] != word[-i -1]:
			return False

	return True

#########################################################################################

# Takes into account if input has spaces, punctuation, etc
# Time: O(n)
# Space: O(1)
def is_palindrome_optimized(candidate):
	"""
	Returns True if input string is a palindrome

	>>> is_palindrome_optimized('a b , c, cba')
	True

	>>> is_palindrome_optimized('abcdcba')
	True
	"""
	start = 0
	end = len(candidate)-1

	while start != end:
		if not candidate[start].isalpha():
			start += 1
		elif not candidate[end].isalpha():
			end -= 1
		else:
			if candidate[start] != candidate[end]:
				return False
			start += 1
			end -= 1
            
	return True

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()