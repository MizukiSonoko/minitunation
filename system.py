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

	pAx, pAy = 1,3
	pBx, pBy = 3,5

	for i in range(8):
		for j in range(8):
			print("|", end="")
			if (pAx, pAy) == (j,i):
				print("い", end="")
			elif (pBx, pBy) == (j,i):
				print("あ", end="")
			else:
				print("　", end="")

		print("|")
