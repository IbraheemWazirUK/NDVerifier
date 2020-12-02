import sys
from src.parser import parse_lines
from src.verifier import verify
def main():
	file_name = sys.argv[1]
	lines = []
	f = open(file_name, "r")
	for line in f:
		lines.append(line)
	
	verify(parse_lines(lines))
	f.close()

main()
