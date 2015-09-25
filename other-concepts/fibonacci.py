def fibonacci(n):
	"""
	Returns n-th number of the Fibonacci sequence

	>>> fibonacci(1)
	1

	>>> fibonacci(10)
	55

	>>> fibonacci([]) is None
	True
	"""
	if not isinstance(n, int):
		return None
	elif n < 2:
		return n
	else:
		return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
	import doctest
	doctest.testmod()