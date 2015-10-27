def balance_parens(parens):
	"""
	Given a string of parentheses, return the string balanced

	>>> balance_parens('(())(')
	'(())()'

	>>> balance_parens('(()')
	'(())'

	>>> balance_parens('((()))')
	'((()))'
	"""
	paren_stack = []
	balanced = ""

	for paren in parens:
		if paren == "(":
			paren_stack.append(paren)
			balanced += paren
		else: # paren == ")"
			if paren_stack:
				paren_stack.pop()
			balanced += paren

	while paren_stack:
		paren_stack.pop()
		balanced += ")"

	return balanced

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()