from enum import Enum

str_to_operation = {'and' : OPERATION.AND, 'or': OPERATION.OR,
'not': OPERATION.NOT, '->': OPERATION.IMPLIES, '<->' : OPERATION.IFF}


class OPERATION(Enum):
	AND = 1
	OR = 2
	NOT = 3
	IMPLIES = 4
	IFF = 5
		
		