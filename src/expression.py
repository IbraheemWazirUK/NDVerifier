from .helper import find_mutual, delete_mutual, print_list, append_no_dupl
class Exp():
	def eliminate(self, e, c):
		pass
	def introduction(self, e, c):
		return False
	def __init__(self, operands):
		self.operands = operands
	def implications(self, cur_true_exps):
		res = []
		for e in cur_true_exps:
			if type(e) is Implies:
				if e.operands[0] == self:
					append_no_dupl(e.operands[1], res)
		return res
	def __eq__(self, other):
		return (type(self) == type(other)) and (self.operands == other.operands) 


class And(Exp):
	def eliminate(self, env, cur_true_exps):
		for i in range(2):
			append_to_env(self.operands[i], env, cur_true_exps)
			append_no_dupl(self.operands[i], cur_true_exps)
	def introduction(self, env, cur_true_exps):
		if (self.operands[0] in cur_true_exps) and (self.operands[1] in cur_true_exps):
			append_to_env(self, env, cur_true_exps)
			append_no_dupl(self, cur_true_exps)
			return True
		return False
	def __str__(self):
		return '(' + self.operands[0].__str__() + ' and ' +  self.operands[1].__str__() + ')'
	
	def __eq__(self, other):
		return type(self) == type(other) and (self.operands == other.operands or self.operands == other.operands[::-1])
class Or(Exp):
	# a -> c and b -> c and a v b ---> c
	def eliminate(self, env, cur_true_exps):
		fst = self.operands[0].implications(cur_true_exps)
		snd = self.operands[1].implications(cur_true_exps)
		for mutual in find_mutual(fst, snd):
			append_to_env(mutual, env, cur_true_exps)
			append_no_dupl(mutual, cur_true_exps)

	def introduction(self, env, cur_true_exps):
		if (self.operands[0] in cur_true_exps) or (self.operands[1] in cur_true_exps):
			append_to_env(self, env, cur_true_exps)
			append_no_dupl(self, cur_true_exps)
			return True
		return False		
	def __str__(self):
		return '(' + self.operands[0].__str__() + ' or ' +  self.operands[1].__str__() + ')'

	def __eq__(self, other):
		return type(self) == type(other) and (self.operands == other.operands or self.operands == other.operands[::-1])



class Not(Exp):
	def eliminate(self, env, cur_true_exps):
		if type(self.operands[0]) is Not:
			append_to_env(self.operands[0].operands[0], env, cur_true_exps)
			append_no_dupl(self.operands[0].operands[0], cur_true_exps)
		if self.operands[0] in cur_true_exps:
			append_to_env(F(), env, cur_true_exps)
			append_no_dupl(F(), cur_true_exps)

	def introduction(self,  env, cur_true_exps):
		if len(env) > 1 and env[-1] and self.operands[0] == env[-1][0]:
			if F() in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				append_to_env(self, env, cur_true_exps)
				append_no_dupl(self, cur_true_exps)
				return True
		return False
	def __str__(self):
		return '(' + 'not ' +  self.operands[0].__str__() + ')'

class Implies(Exp):
	def eliminate(self, env, cur_true_exps):
		if self.operands[0] in cur_true_exps:
			append_to_env(self.operands[1], env, cur_true_exps)
			append_no_dupl(self.operands[1], cur_true_exps)
		if len(find_mutual(find_ifs(self.operands[1], cur_true_exps), find_ors(self.operands[0], cur_true_exps))) > 0:
			append_to_env(self.operands[1], env, cur_true_exps)
			append_no_dupl(self.operands[1], cur_true_exps)	
	def introduction(self, env, cur_true_exps):
		if len(env) > 1 and env[-1] and self.operands[0] == env[-1][0]:
			if self.operands[1] in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				append_to_env(self, env, cur_true_exps)
				append_no_dupl(self, cur_true_exps)
				return True
		return False;

	def __str__(self):
		return '(' + self.operands[0].__str__() + ' -> ' +  self.operands[1].__str__() + ')'

class Iff(Exp):
	def eliminate(self, env, cur_true_exps):
		if self.operands[0] in cur_true_exps:
			append_no_dupl(self.operands[1], env[-1])
			append_no_dupl(self.operands[1], cur_true_exps)
		elif self.operands[1] in cur_true_exps:
			append_no_dupl(self.operands[0], env[-1])
			append_no_dupl(self.operands[0], cur_true_exps)
		if len(find_mutual(find_ifs(self.operands[1], cur_true_exps), find_ors(self.operands[0], cur_true_exps))) > 0:
			append_to_env(self.operands[1], env, cur_true_exps)
			append_no_dupl(self.operands[1], cur_true_exps)	
		elif len(find_mutual(find_ifs(self.operands[0], cur_true_exps), find_ors(self.operands[1], cur_true_exps))) > 0:
			append_to_env(self.operands[0], env, cur_true_exps)
			append_no_dupl(self.operands[0], cur_true_exps)	
	def introduction(self, env, cur_true_exps):
		if len(env) > 1 and env[-1] and self.operands[0] == env[-1][0]:
			if self.operands[1] in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				append_to_env(self, env, cur_true_exps)
				append_no_dupl(self, cur_true_exps)
				return True
		elif len(env) > 1 and env[-1] and self.operands[1] == env[-1][0]:
			if self.operands[0] in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				append_to_env(self, env, cur_true_exps)
				append_no_dupl(self, cur_true_exps)
				return True		
		return False;

	def __str__(self):
		return '(' + self.operands[0].__str__() + ' <-> ' +  self.operands[1].__str__() + ')'
	
	def __eq__(self, other):
		return type(self) == type(other) and (self.operands == other.operands or self.operands == other.operands[::-1])

class Var(Exp):
	def __str__(self):
		return self.operands[0].__str__() 

class T(Exp):
	def __init__(self):
		pass
	def __str__(self):
		return 'true'

	def __eq__(self, other):
		return type(self) == type(other)


class F(Exp):
	def introduction(self, env, cur_true_exps):
		for exp in find_nots(cur_true_exps):
			if exp in cur_true_exps:
				append_to_env(self, env, cur_true_exps)
				append_no_dupl(self, cur_true_exps)
				return True
		return False
	def __init__(self):
		pass
	def __str__(self):
		return 'false'

	def __eq__(self, other):
		return type(self) == type(other)


def find_nots(cur_true_exps):
	res = []
	for exp in cur_true_exps:
		if type(exp) is Not:
			append_no_dupl(exp.operands[0], res)

	return res

def check_false(exp, env, cur_true_exps):
	if F() in cur_true_exps:
		append_to_env(exp, env, cur_true_exps)
		append_no_dupl(exp, cur_true_exps)
		return True

	return False

def find_ifs(exp, cur_true_exps):
	res = []
	for e in cur_true_exps:
		if type(e) is Implies:
			if e.operands[1] == exp:
				append_no_dupl(e.operands[0], res)

		if type(e) is Iff:
			if exp == e.operands[0]:
				append_no_dupl(e.operands[1], res)
			elif exp == e.operands[1]:
				append_no_dupl(e.operands[0], res) 
	return res

def find_ors(exp, cur_true_exps):
	res = []
	for e in cur_true_exps:
		if type(e) is Or:
			if e.operands[0] == exp:
				append_no_dupl(e.operands[1], res)
			elif e.operands[1] == exp:
				append_no_dupl(e.operands[0], res)
	return res

def check_ifs(exp, env, cur_true_exps):
	for e in find_ifs(exp, cur_true_exps):
		if e in cur_true_exps:
			append_to_env(exp, env, cur_true_exps)
			append_no_dupl(exp, cur_true_exps)
			return True


	return False

def append_to_env(exp, env, cur_true_exps):
	if exp not in cur_true_exps: 
		append_no_dupl(exp, env[-1])


def final_check(exp, env, cur_true_exps):
	return check_false(exp, env, cur_true_exps) or check_ifs(exp,env, cur_true_exps)


		