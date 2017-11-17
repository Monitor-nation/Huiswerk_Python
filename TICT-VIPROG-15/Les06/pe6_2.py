zin = input('Voer een zin in met minimaal 10 strings: \n')
lijst = zin.split(' ')
vier_letter_lijst = []

for woord in lijst:
	if len(woord) == 4:
		vier_letter_lijst.append(woord)

print('\n')
print('Lijst met minimaal 10 strings: \n {}' .format(lijst))
print('\n')
print('De nieuw-gemaakte lijst met alle vier-letter strings is: \n {}' .format(vier_letter_lijst))