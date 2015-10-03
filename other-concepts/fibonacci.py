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

#########################################################################################

def _top_down_fibonacci(n, memo):
	if n == 0 or n == 1:
		return n

	if memo[n] == 0:
		memo[n] = _top_down_fibonacci(n-1, memo) + _top_down_fibonacci(n-2, memo)

	return memo[n]

def top_down_fibonacci(n):
	memo = [0]*(n-1)
	return _top_down_fibonacci(n, memo)

#########################################################################################

def bottom_up_fibonacci(n):
	if n == 0 or n == 1:
		return n

	memo = [0]*n
	memo[0] = 0
	memo[1] = 1

	for i in range(2, n):
		memo[i] = memo[i-1] + memo[i-2]

	return memo[n-1] + memo[n-2]

#########################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()