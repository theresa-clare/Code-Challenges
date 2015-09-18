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

if __name__ == "__main__":
	import doctest
	doctest.testmod()