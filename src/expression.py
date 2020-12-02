from .helper import find_mutual, delete_mutual, print_list, append_no_dupl

class Exp():
	def __init__(self):
		pass
		
	def eliminate(self, e, c):
		pass

	def introduction(self, e, c):
		return False

	# returns all expressions x such that self -> x
	def implications(self, cur_true_exps):
		res = []
		for e in cur_true_exps:
			if type(e) is Implies:
				if e.fst == self:
					append_no_dupl(e.snd, res)
		return res

	def __eq__(self, other):
		return type(self) == type(other)

class BinOpExp(Exp):
	def __init__(self, fst ,snd):
		self.fst = fst
		self.snd = snd

	def __eq__(self, other):
		return (type(self) == type(other)) and \
		([self.fst, self.snd] == [other.fst, other.snd] or [self.fst, self.snd] == [other.snd, other.fst]) 

class UnOpExp(Exp):
	def __init__(self, fst):
		self.fst = fst

	def __eq__(self, other):
		return type(self) == type(other) and self.fst == other.fst

class And(BinOpExp):
	# declares fst to be true and snd to be true
	def eliminate(self, env, cur_true_exps):
		for operand in [self.fst, self.snd]:
			append_to_env(operand, env, cur_true_exps)
			append_no_dupl(operand, cur_true_exps)

	# returns true if fst is true and snd is true
	def introduction(self, env, cur_true_exps):
		if (self.fst in cur_true_exps) and (self.snd in cur_true_exps):
			append_to_env(self, env, cur_true_exps)
			append_no_dupl(self, cur_true_exps)
			return True
		return False

	def __str__(self):
		return '(' + self.fst.__str__() + ' and ' +  self.snd.__str__() + ')'

class Or(BinOpExp):
	# a -> c and b -> c and a v b |- c
	def eliminate(self, env, cur_true_exps):
		fst = self.fst.implications(cur_true_exps)
		snd = self.snd.implications(cur_true_exps)
		for mutual in find_mutual(fst, snd):
			append_to_env(mutual, env, cur_true_exps)
			append_no_dupl(mutual, cur_true_exps)

	# returns true if fst is true or snd is true
	def introduction(self, env, cur_true_exps):
		if (self.fst in cur_true_exps) or (self.snd in cur_true_exps):
			append_to_env(self, env, cur_true_exps)
			append_no_dupl(self, cur_true_exps)
			return True
		return False	

	def __str__(self):
		return '(' + self.fst.__str__() + ' or ' +  self.snd.__str__() + ')'

class Not(UnOpExp):
	# not not A |- A
	# A, not A |- false
	def eliminate(self, env, cur_true_exps):
		if type(self.fst) is Not:
			append_to_env(self.fst.fst, env, cur_true_exps)
			append_no_dupl(self.fst.fst, cur_true_exps)
		if self.fst in cur_true_exps:
			append_to_env(F(), env, cur_true_exps)
			append_no_dupl(F(), cur_true_exps)

	# returns true if fst -> false is true
	def introduction(self,  env, cur_true_exps):
		if len(env) > 1 and env[-1] and self.fst == env[-1][0]:
			if F() in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				append_to_env(self, env, cur_true_exps)
				append_no_dupl(self, cur_true_exps)
				return True
		return False

	def __str__(self):
		return '(' + 'not ' +  self.fst.__str__() + ')'


class Implies(BinOpExp):
	# p, p -> q |- q
	# p or q, p -> a, q -> a |- a
	def eliminate(self, env, cur_true_exps):
		if self.fst in cur_true_exps:
			append_to_env(self.snd, env, cur_true_exps)
			append_no_dupl(self.snd, cur_true_exps)
		if len(find_mutual(find_ifs(self.snd, cur_true_exps), find_ors(self.fst, cur_true_exps))) > 0:
			append_to_env(self.snd, env, cur_true_exps)
			append_no_dupl(self.snd, cur_true_exps)	

	# returns true if fst is assumed and snd is derived to be true
	def introduction(self, env, cur_true_exps):
		if len(env) > 1 and env[-1] and self.fst == env[-1][0]:
			if self.snd in env[-1]:
				delete_mutual(env[-1], cur_true_exps)
				env.pop()
				append_to_env(self, env, cur_true_exps)
				append_no_dupl(self, cur_true_exps)
				return True
		return False;

	def __str__(self):
		return '(' + self.fst.__str__() + ' -> ' +  self.snd.__str__() + ')'

	def __eq__(self, other):
		return type(self) == type(other) and [self.fst, self.snd] == [other.fst, other.snd]

# p <-> q treated as p -> q and q -> p
class Iff(Exp):
	def eliminate(self, env, cur_true_exps):
		if self.fst in cur_true_exps:
			append_no_dupl(self.snd, env[-1])
			append_no_dupl(self.snd, cur_true_exps)
		elif self.snd in cur_true_exps:
			append_no_dupl(self.fst, env[-1])
			append_no_dupl(self.fst, cur_true_exps)
		if len(find_mutual(find_ifs(self.snd, cur_true_exps), find_ors(self.fst, cur_true_exps))) > 0:
			append_to_env(self.snd, env, cur_true_exps)
			append_no_dupl(self.snd, cur_true_exps)	
		elif len(find_mutual(find_ifs(self.fst, cur_true_exps), find_ors(self.snd, cur_true_exps))) > 0:
			append_to_env(self.fst, env, cur_true_exps)
			append_no_dupl(self.fst, cur_true_exps)	
	def introduction(self, env, cur_true_exps):
		return Implies(self.fst, self.snd) in cur_true_exps and Implies(self.snd, self.fst) in cur_true_exps;

	def __str__(self):
		return '(' + self.fst.__str__() + ' <-> ' +  self.snd.__str__() + ')'
	
class Var(UnOpExp):
	def __str__(self):
		return self.fst.__str__() 

class T(Exp):
	def __str__(self):
		return 'true'

class F(Exp):
	# A, not A |- false
	def introduction(self, env, cur_true_exps):
		for exp in find_nots(cur_true_exps):
			if exp in cur_true_exps:
				append_to_env(self, env, cur_true_exps)
				append_no_dupl(self, cur_true_exps)
				return True
		return False

	def __str__(self):
		return 'false'

# finds all expressions x such that not x is true
def find_nots(cur_true_exps):
	res = []
	for exp in cur_true_exps:
		if type(exp) is Not:
			append_no_dupl(exp.fst, res)

	return res

# if false has been derived then any expression in the block is true
def check_false(exp, env, cur_true_exps):
	if F() in cur_true_exps:
		append_to_env(exp, env, cur_true_exps)
		append_no_dupl(exp, cur_true_exps)
		return True

	return False

# finds all expressions x such that x -> exp
def find_ifs(exp, cur_true_exps):
	res = []
	for e in cur_true_exps:
		if type(e) is Implies:
			if e.snd == exp:
				append_no_dupl(e.fst, res)

		if type(e) is Iff:
			if exp == e.fst:
				append_no_dupl(e.snd, res)
			elif exp == e.snd:
				append_no_dupl(e.fst, res) 
	return res

# finds all expressions x such that x or exp is true
def find_ors(exp, cur_true_exps):
	res = []
	for e in cur_true_exps:
		if type(e) is Or:
			if e.fst == exp:
				append_no_dupl(e.snd, res)
			elif e.snd == exp:
				append_no_dupl(e.fst, res)
	return res

# returns true if there exists an expression x such that x is true and x -> exp
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


		