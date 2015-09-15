#################################################################################
# 				Exercise 1.2 of Cracking the Coding Interview v5				#
#																				#
#								Reverse a string								#
#################################################################################

# Time: O(n)
# Space: O(n)
def reverse(string):
	"""
	>>> reverse("backpack")
	'kcapkcab'
	"""
	new_string = ""
	for char in string:
		new_string = char + new_string
	return new_string


# Time: O(n)
# Space: O(n)
def reverse_v2(string):
	"""
	>>> reverse_v2("reverse")
	'esrever'
	"""
	length = len(string)
	string_list = list(string)

	for i in range(length/2):
		temp = string_list[i]
		string_list[i] = string_list[length - 1 - i]
		string_list[length - 1 - i] = temp

	return "".join(string_list)


# More pythonic way; switch without temp variable
# Time: O(n)
# Space: O(n)
def reverse_v3(string):
	"""
	>>> reverse_v3("paper")
	'repap'
	"""
	length = len(string)
	string_list = list(string)

	for i in range(length/2):
		string_list[i], string_list[-i - 1] = string_list[-i - 1], string_list[i]

	return "".join(string_list)


# Most pythonic way
def reverse_v4(string):
	"""
	>>> reverse_v4("sweet")
	'teews'
	"""
	return string[::-1]

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()