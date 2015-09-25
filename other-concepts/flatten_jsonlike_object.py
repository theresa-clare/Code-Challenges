def flatten(obj, result_dict, name=''):
	"""
	Flattens the levels of the nested dictionaries and lists given a json-like object

	>>> flatten({'a':1, 'b':2, 'z':[1,2,3]}, {})
	{'a': 1, 'z.2': 3, 'z.1': 2, 'b': 2, 'z.0': 1}

	>>> flatten({'a': 1, 'b': 2, 'z': {'c':1}}, {})
	{'a': 1, 'z.c': 1, 'b': 2}

	>>> flatten({'a':1, 'b':2, 'z':{'a':1, 'b':[10,11,12]}}, {})
	{'a': 1, 'z.a': 1, 'b': 2, 'z.b.1': 11, 'z.b.0': 10, 'z.b.2': 12}

	"""
	if isinstance(obj, dict):
		for key in obj:
			flatten(obj[key], result_dict, name + key + '.')
	elif isinstance(obj, list):
		i = 0
		for item in obj:
			flatten(item, result_dict, name + str(i) + '.')
			i += 1
	else:
		result_dict[name[:-1]] = obj

	return result_dict

def flatten_jsonlike_object(json):
	result_dict = {}
	return flatten(json, result_dict)


#########################################################################################


if __name__ == "__main__":
	import doctest
	doctest.testmod()