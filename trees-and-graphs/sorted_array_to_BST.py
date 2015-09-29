""" 
Cracking the Coding Interview v5: Exercise 4.3

Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height
"""


def sorted_array_to_BST(int_array, start, end):
    if start > end:
        return None

    mid = (start + end)/2
    new_node = Node(int_array[mid])

    new_node.left = sorted_array_to_BST(int_array, start, mid-1)
    new_node.right = sorted_array_to_BST(int_array, mid+1, end)

    return new_node

def sorted_array_to_BST_wrapper(int_array):
    return sorted_array_to_BST(intarray, 0, len(int_array))

#############################################################################

""" Note: creating substrings is expensive in comparison to just indexing,
    like the function above """
def array_to_BST(sorted_list):
	if sorted_list is None:
		return None

	mid = len(sorted_list)/2
	new_node = Node(sorted_list[mid])

	new_node.left = array_to_BST(sorted_list[:mid-1])
	new_node.right = array_to_BST(sorted_list[mid+1:])

	return new_node

#############################################################################

def int_array_to_BST(intarray):
    #use the middle of the array to divide it. this ensures minimal height.
    if len(intarray) == 0:
        return None
    if len(intarray) == 1:
        return BinaryTree(intarray[0])

    mid = len(intarray) / 2
    
    return BinaryTree( intarray[mid], int_array_to_BST(intarray[0:mid]), int_array_to_BST(intarray[mid+1:]))