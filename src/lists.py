par_list = ['(', ')']
if_str_list = ['->', '<->']
if_char_list = ['-', '>', '<']
invalid_chars = ['.', ',']
bin_op_list = ['and', 'or', '->', '<->']
eol_char = ';'

operator_mapper = 
{'and' : (lambda a b : And([a, b])), 'or': (lambda a b : Or([a, b])),
'->' : (lambda a b : Implies([a, b])), '<->' : (lambda a b : Iff([a, b])),
'not' : (lambda a : And([a]))}