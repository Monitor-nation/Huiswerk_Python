import datetime

def get_lopers():
	bestand = open('hardlopers.txt', 'r')
	lopers = bestand.readlines()

	for loper in lopers:
		print(loper)

def lopers_gevens(naam):
	vandaag = datetime.datetime.today()
	vandaag = vandaag.strftime("%a %d %b %Y %H:%M:%S")
	vertrektijd = '11:15'

	outfile = open('hardlopers.txt', 'a')
	outfile.write('{}, {}\n'.format(vandaag, naam))
	outfile.close()

while True:
	get_lopers()
	lopers_naam = input("\nWat is de naam van de loper? ")

	if lopers_naam != "":
		lopers_gevens(lopers_naam)
	else:
		break

datum_tijd= datetime.datetime.today()
tijd_nu = datum_tijd.strftime("%a %d %b %Y %H:%M:%S")
vertrektijd = vertrek['VertrekTijd']
vertrektijd = vertrektijd[tijd_nu]