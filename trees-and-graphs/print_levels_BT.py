def print_levels_BT(node):
	current_level = [node]

	while current_level:
		next_level = []
		for n in current_level:
			print n.data,
			if n.left:
				next_level.append(n.left)
			if n.right:
				next_level.append(n.right)
		print
		current_level = next_level