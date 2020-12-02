from .exceptions import handle_invalid_given_command_exception
from .expression import *
from .helper import print_list, append_no_dupl

def verify(parsed_lines):
	env = [[]] # a list of the lists of true expressions at different levels
	cur_true_exps = [] # a list of all the true expressions 
	ors_list = [] 
	for i in range(len(parsed_lines)):
		#print(i)
		#print_list(cur_true_exps)
		(exp, com) = parsed_lines[i]
		if not exp:
			continue
		if com == 'given':
			if len(env) > 1:
				handle_invalid_given_command_exception(i+1)
			append_to_env(exp, env, cur_true_exps)
			append_no_dupl(exp, cur_true_exps)
			exp.eliminate(env, cur_true_exps)

		elif com == 'ass':
			env.append([])
			append_to_env(exp, env, cur_true_exps)
			append_no_dupl(exp, cur_true_exps)
			exp.eliminate(env, cur_true_exps)

		else:
			if (exp in cur_true_exps) or exp.introduction(env, cur_true_exps) or final_check(exp, env, cur_true_exps):
				exp.eliminate(env, cur_true_exps)
			else:
				handle_false_proof(i+1)

	print('Proof is correct')



def handle_false_proof(line_num):
	print('Mistake in proof on line ', line_num)
	exit()



