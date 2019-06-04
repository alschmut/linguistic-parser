from antlr4 import *
from Java9Lexer import Java9Lexer
from Java9Listener import Java9Listener
from Java9Parser import Java9Parser
from Java9Visitor import Java9Visitor
import sys

class IdentifierListener(Java9Listener):
	identifiers = []

	def getIdentifiers(self):
		return self.identifiers

	def setIdentifiers(self, type, name):
		self.identifiers.append({"type": type, "name": name})

	def enterNormalClassDeclaration(self, ctx):
		self.setIdentifiers("Class", ctx.identifier().getText())
		
	def enterSuperclass(self, ctx):
		self.setIdentifiers("SuperClass", ctx.classType().identifier().getText())

	def enterNormalInterfaceDeclaration(self, ctx):
		self.setIdentifiers("Normal Interface", ctx.identifier().getText())

	def enterAnnotationTypeDeclaration(self, ctx):
		self.setIdentifiers("Annotation Interface", ctx.identifier().getText())
		
	def enterVariableDeclaratorId(self, ctx):
		self.setIdentifiers("Variable", ctx.identifier().getText())

	def enterMethodDeclarator(self, ctx):
		self.setIdentifiers("Method", ctx.identifier().getText())
		
	def enterIdentifier(self, ctx):
		self.setIdentifiers("Identifier", ctx.getText())

def txtget(filename):
	try:
		# open file read-only, get file content and close
		with open(filename, 'r') as file:
			file_content = file.read()
			return file_content

	except Exception as err:
		print("Could not open file: ", type(err), ":", err)
		return None

def printIdentifier(identifiers):
	for identifier in sorted(identifiers, key=lambda k: k["type"]):
		print(identifier["type"] + ": " + identifier["name"])
	
def main():
	input_stream = InputStream(txtget("AJavaExample.java"))
	lexer = Java9Lexer(input_stream)
	stream = CommonTokenStream(lexer)
	parser = Java9Parser(stream)
	tree = parser.compilationUnit()
	listener = IdentifierListener()
	walker = ParseTreeWalker()
	walker.walk(listener, tree)
	identifiers = listener.getIdentifiers()
	printIdentifier(identifiers)

if __name__ == '__main__':
    main()
