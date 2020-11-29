def handle_invalid_str_exception(line_num):
	print('invalid character on line ', line_num)
	exit()

def handle_eol_exception(line_num):
	print('invalid string after end of line on line ', line_num)
	exit()