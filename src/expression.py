class Exp():
	def __init__(self, operands):
		self.operands = operands

class And(Exp):
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
	

		