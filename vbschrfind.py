import re

teste = 'virus'

def formataporra(string):
	formatedArray = re.findall('[0-9]+', string)
	print(" ".join(formatedArray))


formataporra(teste)