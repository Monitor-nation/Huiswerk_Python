import csv

#Kolomkoppen inlezen met DictReader!
with open('producten2.csv', 'r', newline='') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    maxprijs = 0

    for row in reader:
        prijs = int(row['Prijs'])
        if prijs > maxprijs:
            maxprijs = prijs
            maxNaam = row['Naam']

print('{} {}' .format(maxprijs, maxNaam))


