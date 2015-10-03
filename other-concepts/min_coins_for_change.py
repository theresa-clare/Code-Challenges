"""
Find minimum number of ocins that make a given value

Given a value V, if we want to make change for V cents, and we have infinite
supply of each of C = [C1, C2, ..., Cm] valued coins, what is the minimum number
of coins to make the change?

http://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

Example:
	Input: 		coins = [25, 10, 5], V = 30
	Output:		3

	Input:		coins = [9, 6, 5, 1], V = 11
	Output:		2
"""

def min_coins_for_change(coins, n, value):
	if value == 0:
		return 0

	res = 0

	for coin in coins:
		if coin <= value:
			sub_res = min_coins_for_change(coins, n, value-coin)
			if sub_res + 1 < res:
				res = sub_res + 1

	return res
