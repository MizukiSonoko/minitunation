
class Parser:
	def __init__(self):
		self.rules = []


	def parse(self, tokens):
		status = 0
		obj = []
		inv = False
		for i in range(len(tokens)):
			t = tokens[i]
			if status == 1:
				if t[1] in {"should"}:
					status = 2
				else:
					print("Syntax error in Status ["+t[1]+"]")
					quit()
			elif status == 2:
				if t[1] in {"not"}:
					status = 3
					inv = True
				else:
					verb = t[1]
					status = 4
			elif status == 3:
				if t[0] == "ID":
					verb = t[1]
					status = 4
			elif status == 4:
				if t[0] == "PERIOD":
					self.rules.append([subject,verb,obj,inv])
					status = 0
					obj = []
					inv = False
				else:
					obj.append(t[1])

			elif status == 5:
				subject_if = t[1]
				status = 6
			elif status == 6:
				verb_if = t[1]
				status = 7
			elif status == 8:
				if t[0] == "COMMA":
					status = 0
				else:
					obj_if.append(t[1])

			elif status == 0:
				if t[0] == "FIN":
					print("Finish!")
				else:
					subject = t[1]
					status = 1

	def dump(self):
		for i in self.rules:
			print(i)