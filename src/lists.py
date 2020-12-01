from .expression import *

par_list = ['(', ')']
if_str_list = ['->', '<->']
if_char_list = ['-', '>', '<']
invalid_chars = ['.', ',']
bin_op_list = ['and', 'or', '->', '<->']
eol_char = ';'
command_list = ['given, ass']
tf_list = ['true', 'false']
special_chars = ['\n', '\\', '\r', '\t', '\'']
precedence_map = \
{'not' : 1, 'and' : 2, 'or' : 3, '->' : 4, '<->' : 5, ')' : 6}
operator_mapper = {'and' : (lambda a, b : And([a, b])), 'or': (lambda a, b : Or([a, b])), \
'->' : (lambda a, b : Implies([a, b])), '<->' : (lambda a, b : Iff([a, b])), \
'not' : (lambda a : Not([a])), 'true' : (lambda : T()), 'false': (lambda: F())}