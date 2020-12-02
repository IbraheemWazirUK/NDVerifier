# returns true if x contains an element fron elem_list
def contains_elem(elem_list, x):
	for elem in elem_list:
		if elem in x:
			return True
	return False

# checks that elem is not None and then appends
def check_and_append(lst, elem):
	if elem:
		lst.append(elem)

# returns a list of common elements of lists l1 and l2
def find_mutual(l1, l2):
	return [elem for elem in l1 if elem in l2]

# deletes all common elements of l1 and l2 from l2
def delete_mutual(l1, l2):
	union = find_mutual(l1, l2)
	for elem in union:
		l2.remove(elem)

# for testing purposes
def print_list(l):
	res = []
	for i in l:
		res.append(i.__str__())
	print(res)

# appends elem to list l1 while avoiding duplication
def append_no_dupl(elem, l1):
	l1.append(elem) if elem not in l1 else None