def pretty_print_json(json, level):
	if not json:
		return

	if isinstance(json, list):
		print " "*level*4, "["
		for element in json:
			pretty_print_json(element, level+1)
		print " "*level*4, "]"

	elif isinstance(json, dict):
		print " "*level*4, "{"
		for k,v in json.iteritems():
			pretty_print_json("{0}: {1}".format(k,v), level+1)
		print " "*level*4, "}"

	else:
		print " "*level*4, json