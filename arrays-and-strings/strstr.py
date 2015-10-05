"""
The strstr function locates a specified substring within a source string.

http://articles.leetcode.com/2010/10/implement-strstr-to-find-substring-in.html
"""

def strstr(string, substring):
	"""
	Returns index of the first occurrence of substring within string; -1 otherwise

	>>> strstr('awrtwertwertaaaaabcwertwertwertw', 'aaaaabc')
	12

	>>> strstr('abcdefabc', 'ghijk')
	-1
	"""
	for i in range(len(string)-len(substring)+1):
		if string[i] == substring[0]:
			start = 0
			while start < len(substring) and string[i+start] == substring[start]:
				start += 1
			if start == len(substring):
				return i
	return -1

#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()