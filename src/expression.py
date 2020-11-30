class Exp():
	def eliminate(self):
		return []
	def __init__(self, operands):
		self.operands = operands
	def __eq__(self, other):
		return (self.operands == other.operands) and (type(self) == type(other)) 

class And(Exp):
	def eliminate(self):
		return [self.operands[0], self.operands[1]]
	def introduction(self, env, cur_true_exps):
		if (self.operands[0] in cur_true_exps) and (self.operands[1] in cur_true_exps):
			env[-1].append(self)
			cur_true_exps.append(self)
			return true
		return false
	def __str__(self):
		return '(' + self.operands[0].__str__() + ' and ' +  self.operands[1].__str__() + ')'

class Or(Exp):
	def __str__(self):
		return '(' + self.operands[0].__str__() + ' or ' +  self.operands[1].__str__() + ')'
class Not(Exp):
	def __str__(self):
		return '(' + 'not ' +  self.operands[0].__str__() + ')'
class Implies(Exp):
	def __str__(self):
		return '(' + self.operands[0].__str__() + ' -> ' +  self.operands[1].__str__() + ')'
class Iff(Exp):
	def __str__(self):
		return '(' + self.operands[0].__str__() + ' <-> ' +  self.operands[1].__str__() + ')'
class Var(Exp):
	def __str__(self):
		return '(' + self.operands[0].__str__() + ')'
	
		