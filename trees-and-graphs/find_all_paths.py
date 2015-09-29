""" 
Offset of CTCIv5: Exercise 4.2 (find out whether there is a path route between two nodes)

Find ***all*** paths between two nodes
"""

def find_all_paths(graph, start, end, path=[]):
	path += [start]

	if start == end:
		return [path]

	if not graph.has_key(start):
		return []

	paths = []

	for node in graph[start]:
		if node not in path:
			new_path = find_all_paths(graph, node, end, path)
			for newpath in newwpaths:
				paths.append

	return paths