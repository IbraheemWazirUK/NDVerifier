from .lexer import get_words
from .lists import * 
from .exceptions import \
handle_double_command_exception, handle_bracket_mismatch_exception, \
handle_invalid_arguments_exception 
from .expression import Var
from .helper import print_list
# returns a tuple containing a list of expressions and a line command if it exists
def parse(line, line_num):
	words = get_words(line, line_num)
	op_stack = []
	exp_stack = []
	command = ''
	for word in words:
		#print_list(op_stack)
		#print_list(exp_stack)
		if word == eol_char:
			while (op_stack):
				if op_stack[-1] == '(':
					handle_bracket_mismatch_exception(line_num)
				add_exp_to_stack(op_stack, exp_stack, line_num)
			break
		elif word == '(':
			op_stack.append('(')
		elif word == ')':
			if not op_stack:
				handle_bracket_mismatch_exception(line_num)
			while (op_stack[-1] != '('):
				add_exp_to_stack(op_stack, exp_stack, line_num)
				if not op_stack:
					handle_bracket_mismatch_exception(line_num)
			op_stack.pop();
		elif word in command_list:
			if command:
				handle_double_command_exception(line_num)
			command = word
		elif word in tf_list:
			exp_stack.append(operator_mapper[word]())
		elif word in precedence_map:
			if op_stack:
				op = op_stack[-1]
				while (op_stack and op != '(' and precedence_map[op] < precedence_map[word] ):
					op = op_stack[-1];
					add_exp_to_stack(op_stack, exp_stack, line_num)
			op_stack.append(word)
		else:
			exp_stack.append(Var([word]))
	if exp_stack:
		# print_list(exp_stack)
		return (exp_stack[0], command)

	else: 
		return (None, None)

def add_exp_to_stack(op_stack, exp_stack, line_num):
	op = op_stack[-1]
	if op != '(':
		op = op_stack.pop()
	if op == ')':
		if not op_stack:
			handle_bracket_mismatch_exception(line_num)
		while (op_stack[-1] != ')'):
			add_exp_to_stack(exp_stack, op_stack, line_num)
			if not op_stack:
				handle_bracket_mismatch_exception(line_num)
	if op in bin_op_list:
		if not exp_stack:
			handle_invalid_arguments_exception(line_num)
		snd = exp_stack.pop()
		if not exp_stack:
			handle_invalid_arguments_exception(line_num)
		fst = exp_stack.pop()
		exp_stack.append(operator_mapper[op](fst, snd))
	elif op in un_op_list:
		if not exp_stack:
			handle_invalid_arguments_exception(line_num)
		fst = exp_stack.pop()
		exp_stack.append(operator_mapper[op](fst))

def parse_lines(lines):
	res = []
	for i in range(len(lines)):
		temp = parse(lines[i], i+1)
		res.append(temp)
	return res



