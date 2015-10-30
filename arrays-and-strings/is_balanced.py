"""
Given an expression from a string, write a program to examine whether the pairs
and the orders are correct in the expression. Return True if in right order;
return False otherwise
"""

# Time: O(1)
# Space: O(1)
def is_parens(char):
	"""
	Returns True if character is a type of parentheses; returns False otherwise

	>>> is_parens("{")
	True

	>>> is_parens("c")
	False

	>>> is_parens("char")
	False
	"""
	parens = {"(", ")", "[", "]", "{", "}"} # can make global variable instead

	if char in parens:
		return True
	return False

# Time: O(n)
# Space: O(n)
def is_balanced(parens):
	"""
	Given an expression, returns True if the parentheses are balanced

	>>> is_balanced("{}[()]")
	True

	>>> is_balanced("([)[]")
	False

	>>> is_balanced("(c)")
	True
	"""
	matching_parens = {
		")": "(",
		"]": "[",
		"}": "{"
	}
	parens_stack = []

	for paren in parens:
		if not is_parens(paren):
			continue
		
		if paren not in matching_parens: # if opening parentheses
			parens_stack.append(paren)
		else:
			if parens_stack[-1] != matching_parens[paren]:
				return False
			else:
				parens_stack.pop()

	if parens_stack:
		return False
	return True

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()