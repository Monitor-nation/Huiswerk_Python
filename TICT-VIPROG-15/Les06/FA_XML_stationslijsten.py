def toon_aantalkluizen_vrij():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    aantalkluizen = len(kluizendata)
    aantalvrij = 12 - aantalkluizen
    print(aantalvrij)

def nieuwe_kluis():
    print(2)

def kluis_openen():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is je nummer')
    code = input('Wat is je code')
    #standaard staat kluis op false
    gegevensCorrect = False
    #per regel een list met gegevens
    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringkluisnummer = gegevensvan1kluis[0]
        kluiscode = gegevensvan1kluis[1].strip()
        #contoleren of stringkluisnummer gelijk is aan stringnummer en kluiscode aan code
        if stringnummer == stringkluisnummer and code == kluiscode:
            gegevensCorrect = True
    if gegevensCorrect:
        print('De kluis wordt geopend')
    else:
        print('De kluis wordt niet geopend')

print('1: hoeveel vrij')
print('2: nieuwe kluis')
print('3: kluis openen')
keuze= eval(input('maakkeuze'))

if keuze == 1:
    toon_aantalkluizen_vrij()
elif keuze == 2:
    nieuwe_kluis()
else:
    kluis_openen()