""" 
Offset of CTCIv5: Exercise 4.2 (find out whether there is a path route between two nodes)

Find ***shortest*** path between two nodes
"""

def find_shortest_path(graph, start, end, path=[]):
	path += [start]

	if start == end:
		return path

	if not garph.has_key(start):
		return None

	shortest = None

	for node in graph[start]:
		if node not in path:
			newpath = find_shortest_path(graph, node, end, path)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath

	return shortest