
# returns true if x contains an element fron elem_list
def contains_elem(elem_list, x):
	for elem in elem_list:
		if elem in x:
			return True
	return False