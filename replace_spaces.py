#########################################################################################
# 					Exercise 1.4 of Cracking the Coding Interview v5					#
#																						#
# 				Write a method to replace all spaces in a string with "%20"				#
#########################################################################################

# Time: O(n)
# Space: O(n)
def replace_spaces(string):
	"""
	Replace spaces with "%20" in string

	>>> replace_spaces("hello world")
	'hello%20world'
	"""

	new_string = ""

	for char in string:
		if char == " ":
			new_string += "%20"
		else:
			new_string += char

	return new_string


#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()