from .helper import find_mutual, delete_mutual

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
					res.append(e.operands[1])
		return res
	def __eq__(self, other):
		return (self.operands == other.operands) and (type(self) == type(other)) 

class And(Exp):
	def eliminate(self, env, cur_true_exps):
		for i in range(2):
			env[-1].append(self.operands[i])
			cur_true_exps.append(self.operands[i])
	def introduction(self, env, cur_true_exps):
		if (self.operands[0] in cur_true_exps) and (self.operands[1] in cur_true_exps):
			env[-1].append(self)
			cur_true_exps.append(self)
			return True
		return False
	def __str__(self):
		return '(' + self.operands[0].__str__() + ' and ' +  self.operands[1].__str__() + ')'

class Or(Exp):
	# a -> c and b -> c and a v b ---> c
	def eliminate(self, env, cur_true_exps):
		fst = self.operands[0].implications(cur_true_exps)
		snd = self.operands[1].implications(cur_true_exps)
		for mutual in find_mutual(fst, snd):
			env[-1].append(mutual)
			cur_true_exps.append(mutual)

	def introduction(self, env, cur_true_exps):
		if (self.operands[0] in cur_true_exps) or (self.operands[1] in cur_true_exps):
			env[-1].append(self)
			cur_true_exps.append(self)
			return True
		return False		
	def __str__(self):
		return '(' + self.operands[0].__str__() + ' or ' +  self.operands[1].__str__() + ')'


class Not(Exp):
	def eliminate(self, env, cur_true_exps):
		if type(self.operands[0]) is Not:
			cur_true_exps.append(self.operands[0].operands[0])
			env[-1].append(self.operands[0].operands[0])
		if self.operands[0] in cur_true_exps:
			cur_true_exps.append(F())
			env[-1].append(F())

	def introduction(self,  env, cur_true_exps):
		if len(env) > 1 and env[-1] and self.operands[0] == env[-1][0]:
			if F() in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				env[-1].append(self)
				cur_true_exps.append(self)
				return True
		return False
	def __str__(self):
		return '(' + 'not ' +  self.operands[0].__str__() + ')'

class Implies(Exp):
	def eliminate(self, env, cur_true_exps):
		if self.operands[0] in cur_true_exps:
			env[-1].append(self.operands[1])
			cur_true_exps.append(self.operands[0])
	def introduction(self, env, cur_true_exps):
		if len(env) > 1 and env[-1] and self.operands[0] == env[-1][0]:
			if self.operands[1] in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				env[-1].append(self)
				cur_true_exps.append(self)
				return True
		return False;

	def __str__(self):
		return '(' + self.operands[0].__str__() + ' -> ' +  self.operands[1].__str__() + ')'

class Iff(Exp):
	def eliminate(self, env, cur_true_exps):
		if self.operands[0] in cur_true_exps:
			env[-1].append(self.operands[1])
			cur_true_exps.append(self.operands[1])
		elif self.operands[1] in cur_true_exps:
			env[-1].append(self.operands[0])
			cur_true_exps.append(self.operands[0])

	def introduction(self, env, cur_true_exps):
		if len(env) > 1 and env[-1] and self.operands[0] == env[-1][0]:
			if self.operands[1] in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				env[-1].append(self)
				cur_true_exps.append(self)
				return True
		elif len(env) > 1 and env[-1] and self.operands[1] == env[-1][0]:
			if self.operands[0] in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				env[-1].append(self)
				cur_true_exps.append(self)
				return True		
		return False;

	def __str__(self):
		return '(' + self.operands[0].__str__() + ' <-> ' +  self.operands[1].__str__() + ')'


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
		for exp in find_nots:
			if exp in cur_true_exps:
				env[-1].append(self)
				cur_true_exps.append(self)
				return True
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
			res.append(exp.operands[0])

	return res

def check_false(exp, env, cur_true_exps):
	if F() in cur_true_exps:
		env[-1].append(exp)
		cur_true_exps.append(cur_true_exps)
		return True

	return False


		