import csv

with open('inloggen.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    #writer.writerow(('number', 'name'))

    while True:
        naam = input('Wat is je naam ')
        if naam == 'einde':
            break
        voorLetter = input('Wat is je voorletter: ')
        geboorteDatum = input('Wat is je geboortedatum: ')
        email = input('Wat is je email: ')

        #Dit moet je wegschrijven door(dubbele haken voor tupel):
        writer.writerow((naam, voorLetter,geboorteDatum,memoryview))
