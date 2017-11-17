bestand = open('kaartnummers.txt', 'r')
regels = bestand.readlines()
bestand.close()

for regel in regels:
	kaartinfo = regel.split(',')
print('{} heeft kaartnummer:{}' .format(kaartinfo[1].strip(), kaartinfo[0]))