"""
Minimum number of jumps to reach end


Given an array of integers where each element represents the max number of steps
that can be made forward from that element. Write a function to return the minimum
number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then cannot move through that element.

Example:
	Input:		[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
	Output:		3 (1 -> 3 -> 8 -> 9)

http://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/
"""

# from http://www.careercup.com/question?id=24669663
# recursive with memoization
def min_jumps_to_end(arr, i, path):
	n_steps = float('inf')
	m = arr[i]

	# if can reach the last element with one jump
	if i + m >= len(arr) - 1:
		path[i] = 1
		return 1
	# test every possible jump from 1 to max possible value
	else:
		for j in range(i+1, i+m+1):
			if path[j] is None:
				# will assign a value to path[j]
				min_jumps_to_end(arr, j, path)
			if path[j] < n_steps:
				n_steps = path[j]

		# add to recursive value 1 for this jump
		path[i] = n_steps + 1

		return n_steps + 1

def min_jumps_to_end_wrapper(arr):
	n = len(arr)
	path = []*n

	if n == 1:
		return 0

	return min_jumps_to_end(arr, 0, path)

#########################################################################################

# http://www.careercup.com/question?id=24669663
# greedy without memoization
def greedy_min_jumps_to_end(a, i=0, step_count=0):
	best_step = i
	best_possible = i
	n = len(a)

	if i == n-1:
		return 0

	m = a[i]

	if m+i >= n-1:
		return step_count + 1

	for j in range(i+1, min(n-1, i+m+1)):
		s = a[j] + j
		if s > best_possible:
			best_possible = s
			best_step = j

	if best_step == i:
		return float('inf')
	else:
		return greedy_min_jumps_to_end(a, best_step, step_count+1)