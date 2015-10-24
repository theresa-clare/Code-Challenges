# Time: O(n)
# Space: O(n)
def reverse_number(num):
	""" 
	Given a number, return the number reversed

	>>> reverse_number(1234)
	4321

	>>> reverse_number(0)
	0

	>>> reverse_number(-1234)
	-4321
	"""
	rev_number = 0
	negative_flag = 0

	if num < 0:
		negative_flag = 1
		num *= -1

	while num > 0:
		mod = num % 10
		rev_number *= 10
		rev_number += mod
		num /= 10

	if negative_flag == 1:
		return -rev_number
	else:
		return rev_number

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()