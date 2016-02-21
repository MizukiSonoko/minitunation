import re

class Lexer:

	def __init__(self):
		self.tokens = []
		self.row_str = ""

	def __isNumber( self, c):
		return re.match('[0-9]', c)

	def __isLetter( self, c):
		return re.match('[a-zA-Z]', c)

	def __isAlphanumeric( self, c):
		return re.match('[a-zA-Z0-9]', c)

	def __clean(self):
		del self.tokens[:]
		row_str = "";
	
	def loader( self, filename):
		self.__clean()

		file = open(filename, 'r')
		if not file:
			print("File not found!!")

		for line in file:
			self.row_str += line
			
		file.close()

	def lexer(self, filename):
		self.loader(filename)
		status = 0
		buffer = ""
		for i in range(len(self.row_str)):
			c = self.row_str[i]
			if status == 1:
				if c == '"':
					self.tokens.append(["NAME",buffer])
					buffer = ""
					status = 0
				else:
					buffer += c					
				i+= 1
			elif status == 2:
				if self.__isNumber(c) and  c != '.':
					if "." in buffer:
						self.tokens.append(["RNUM",buffer])
					else:
						self.tokens.append(["NUM",buffer])
					buffer = ""
					status = 0
				elif self.__isNumber(c):
					buffer += c
					i += 1
			elif status == 3:
				if self.__isAlphanumeric(c):
					buffer += c
					i += 1
				else:
					self.tokens.append(["ID",buffer])
					buffer = "";
					status = 0;

			elif status == 4:
				if '\n' == c:
					status = 0

			if status == 0:
				if self.__isLetter(c):
					buffer += c
					status = 3
					i-= 1
				elif self.__isAlphanumeric(c):
					buffer += c
					status = 2
					i-= 1
				else:
					if c in { ' ', '\t', '\n', '\r'}:
						pass
					elif c =='"':
						status = 1
					elif c == '(':
						self.tokens.append(["LPARENT","("])
					elif c == ')':
						self.tokens.append(["RPARENT",")"])
					elif c == ']':
						self.tokens.append(["RBRACKET","]"])
					elif c == '[':
						self.tokens.append(["LBRACKET","["])
					elif c == '}':
						self.tokens.append(["RCBRACKET","}"])
					elif c == '{':
						self.tokens.append(["LCBRACKET","{"])
					elif c == '>':
						self.tokens.append(["RABRACKET",">"])
					elif c == '<':
						self.tokens.append(["LABRACKET","<"])
					elif c == ';':
						self.tokens.append(["SEMICOLON",";"])
					elif c == ':':
						self.tokens.append(["COLON",":"])
					elif c == ',':
						self.tokens.append(["COMMA",","])
					elif c == '.':
						self.tokens.append(["PERIOD","."])
					elif c == '^':
						self.tokens.append(["CARET","^"])
					elif c == '#':
						status = 4
					elif c == '~':
						self.tokens.append(["WAVY","~"])
					elif c == '@':
						self.tokens.append(["AT_SIGN","@"])
					elif c == '=':
						self.tokens.append(["EQUAL","="])
					elif c == '+':
						self.tokens.append(["ADD","+"])
					elif c == '-':
						self.tokens.append(["SUB","-"])
					elif c == '*':
						self.tokens.append(["MUL","*"])
					elif c == '/':
						self.tokens.append(["DIV","/"])
					elif c == '!':
						self.tokens.append(["EXCLAMATION","!"])
					else:
						print("Error! ["+ c +"]")
					i += 1;
						
			
		self.tokens.append(["FIN","FIN"])

	def dump(self):
		for i in self.tokens:
			print(i)

	def  token(self):
		return self.tokens












