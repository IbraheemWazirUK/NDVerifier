from .lists import *
from .helper import contains_elem, check_and_append
from .exceptions import *
def get_words(line, line_num):
	line = [c for c in line if (not c in special_chars)]
	res = []
	cur_str = ''
	eol_flag = False
	for char in line:
		#print(res)
		if char == ' ':
			check_for_invalid_chars(cur_str, line_num)
			check_and_append(res, cur_str)
			cur_str = ''
			continue
		if eol_flag:
			handle_eol_exception(line_num)		
		if char == '(':
			if len(cur_str) > 0:
				handle_invalid_str_exception(line_num)
			res.append('(')
			continue
		if char == ')':
			check_and_append(res, cur_str)
			cur_str = ')'
			continue
		if char == eol_char:
			check_and_append(res, cur_str)
			cur_str = eol_char
			eol_flag = True
			continue
		cur_str += char
	check_for_invalid_chars(cur_str, line_num)
	check_and_append(res, cur_str)
	if res and res[-1] != eol_char:
		handle_missing_eol_exception(line_num)
	return res


def check_for_invalid_chars(x, line_num):
	if contains_elem(invalid_chars, x):
		handle_invalid_str_exception(line_num)
	if contains_elem(if_char_list, x):
		if not (x in if_str_list):
			handle_invalid_str_excpetion(line_num)
	if ')' in x:
		if x.count(')') != len(x):
			handle_invalid_str_exception(line_num)


