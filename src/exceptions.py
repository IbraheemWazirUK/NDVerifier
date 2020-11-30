def handle_invalid_str_exception(line_num):
	print('invalid character on line ', line_num)
	exit()

def handle_eol_exception(line_num):
	print('invalid string after end of line on line ', line_num)
	exit()

def handle_missing_eol_exception(line_num):
	print('missing end of line character on line ', line_num)
	exit()

def handle_double_command_exception(line_num):
	print('two commands in the same line on line ', line_num)
	exit()

def handle_invalid_arguments_exception(line_num):
	print('invalid arguments for operator on line ', line_num)
	exit()

def handle_bracket_mismatch_exception(line_num):
	print('bracket mismatch on line ', line_num)
	exit()

def handle_invalid_given_command_exception(line_num):
	print('given command inside assumption block on line ', line_num)