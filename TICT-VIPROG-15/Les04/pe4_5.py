
def kwadraten_som(grondgetallen):
    antwoord = 0
    for getal in grondgetallen:
        if getal > 0:
            kwadraat = getal**2
            antwoord = antwoord + kwadraat
    return antwoord


print(kwadraten_som([4, 5, 3, -81]))