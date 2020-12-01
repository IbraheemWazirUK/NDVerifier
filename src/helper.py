
# returns true if x contains an element fron elem_list
def contains_elem(elem_list, x):
	for elem in elem_list:
		if elem in x:
			return True
	return False


def check_and_append(lst, elem):
	if elem:
		lst.append(elem)


def find_mutual(l1, l2):
	return list(set(l1) & set(l2))

def delete_mutual(l1, l2):
	union = find_mutual(l1, l2)
	for elem in union:
		l2.remove(elem)

