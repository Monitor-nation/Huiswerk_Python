def code(invoerstring):
	nieuwestring = ''

	for letter in invoerstring:
		nieuweASCII = ord(letter) + 3
		nieuwekar = chr(nieuweASCII)
		nieuwestring += nieuwekar
	return nieuwestring


naam = input('Wat is jouw naam? ')
beginstaion = input('Van welke station vertrek je? ')
eindstation = input('Bij welke station ga je uitstappen? ')
invoerstring = naam + beginstaion + eindstation

print()
print(invoerstring)
print(code(invoerstring))