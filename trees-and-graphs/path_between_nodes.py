"""
Cracking the Coding Interview v5: Exercise 4.2

Given a directed graph, design an algorithm to find out whether there is a path route between two nodes
"""

# find a path between two nodes, if one exists
def path_between_nodes(graph, start, end, path=[]):
	path += [start]

	if start == end:
		return path

	if not start in graph: #graph.has_key(start):
		return None

	for node in graph[start]:
		if node not in path:
			new_path = path_between_nodes(graph, node, end, path)
			if new_path:
				return new_path

	return None

#################################################################################################################################################

"""Cracking the Coding Interview version: simple graph traversal, check if the other node is found, mark other nodes as "visited" """

# iterative implementation of breadth first search
from enum import Enum

class State(Enum):
	Unvisited = 1
	Visited = 2
	Visiting = 3

def search_path(graph, start, end):
	if start == end:
		return True

	ll_queue = LinkedList()

	for u in graph.getNodes():
		u.state = State.Unvisited

	start.state = State.Visiting
	q.add(start)
	Node u

	while not q.isEmpty():
		u = q.dequeue() #remove first
		if u != None:
			for v in u.getAdjacent():
				if v.state = State.Unvisited:
					if v == end:
						return True
					else:
						v.state = State.Visiting
						q.add(v)
			u.state = State.Visited

	return False