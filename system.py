from lexer import *
from parser import *


if __name__ == "__main__":
	import sys
	argv = sys.argv
	if len(argv) <= 1:
		print("Pls rule file")
		quit()

	l = Lexer()
	l.lexer(argv[1])
	token = l.token()

	p = Parser()
	p.parse(token)

	p.dump()