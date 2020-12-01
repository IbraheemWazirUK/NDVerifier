from .exceptions import handle_invalid_given_command_exception
from .expression import *
from .helper import print_list

def verify(parsed_lines):
	env = [[]] # a list of the lists of true expressions at different levels
	cur_true_exps = [] # a list of all the true expressions 
	for i in range(len(parsed_lines)):
		print_list(cur_true_exps)
		(exp, com) = parsed_lines[i]
		if com == 'given':
			if len(env) > 1:
				handle_invalid_given_command_exception(i+1)
			env[-1].append(exp)
			cur_true_exps.append(exp)
			exp.eliminate(env, cur_true_exps)

		elif com == 'ass':
			env.append([])
			env[-1].append(exp)
			cur_true_exps.append(exp)
			exp.eliminate(env, cur_true_exps)

		else:
			if (exp in cur_true_exps) or exp.introduction(env, cur_true_exps) or check_false(exp, env, cur_true_exps):
				exp.eliminate(env, cur_true_exps)
			else:
				handle_false_proof(i+1)

	print('Proof is correct')



def handle_false_proof(line_num):
	print('Mistake in proof on line ', line_num)
	exit()



