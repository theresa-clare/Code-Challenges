def get_subsets(s):
	"""
	Given a list of elements, returns a list of all possible subsets

	>>> get_subsets(['a', 'b', 'c'])
	[['a', 'b', 'c'], ['b', 'c'], ['a', 'c'], ['c'], ['a', 'b'], ['b'], ['a'], []]

	>>> get_subsets([])
	[[]]
	"""
	if len(s) < 1:
		return [[]]

	subsets = get_subsets(s[1:])
	res = []

	for ss in subsets:
		res.append([s[0]] + ss)
		res.append(ss)

	return res

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()