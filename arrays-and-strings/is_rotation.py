#########################################################################################
# 					Exercise 1.8 of Cracking the Coding Interview v5					#
#																						#
# Assume you have a method isSubstring which checks if one word is 	a substring of 		#
# another. Given two strings, s1 and s2, write code	to check if s2 is a rotation of s2 	#
# using only one call to isSubstring. 													#
#	e.g. "waterbottle"																	#
#		 "erbottlewat"																	#
#########################################################################################

# Without using isSubstring
def is_rotation(s1, s2):
	"""
	>>> is_rotation("waterbottle", "erbottlewat")
	True

	>>> is_rotation("something", "something")
	True

	>>> is_rotation("cat", "dog")
	False
	"""
	for i in range(len(s1)):
		if s1 == s2:
			return True
		s2 = s2[1:] + s2[0]
	return False

# using isSubstring from Cracking the Coding Interview
def is_rotation_v2(s1, s2):
	if len(s1) == len(s2) and len(s1) > 0:
		s1s1 = s1 + s1
		return isSubstring(s1s1, s2)
	return False

#################################################################################

if __name__ == "__main__":
	import doctest
	doctest.testmod()