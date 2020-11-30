from exceptions import handle_invalid_given_command_exception
from expression import *
def verify(parsed_lines):
	env = [[]] # a list of the lists of true expressions at different levels
	level = 0
	cur_true_exps = [] # a list of all the 
	for i in range(len(parsed_lines)):
		(exp, com) = parsed_line[i]
		if com == 'given':
			if level > 0:
				handle_invalid_given_command_exception(i+1)
			env[level].append(exp)
			cur_true_exps.append(exp)
			for e in exp.eliminate():
				env[level].append(e)
				cur_true_exps.append(e)

		elif com == 'ass':
			env.append([])
			level+=1
			env[level].append(exp)
			cur_true_exps.append(exp)
			for e in exp.eliminate():
				env[level].append(e)
				cur_true_exps.append(e)

		else:
			if not ((exp in cur_true_exps) or exp.introduce(env, cur_true_exps) or check(exp, env, cur_true_exps)):
				handle_false_proof(i+1)



def handle_false_proof(line_num):
	print('Mistake in proof on line, ' line_num)
	exit()



