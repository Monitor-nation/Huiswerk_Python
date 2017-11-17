cijferICOR = 7.5
cijferPROG = 7.5
cijferCSN = 7.5
cijferPunt = 30
tcijfers = cijferICOR + cijferPROG + cijferCSN

#het gemiddelde van de variabelen cijferICOR, cijferPROG en cijferCSN
gemiddelde = tcijfers / 3
print(gemiddelde)

#de totale beloning voor deze drie cursussen
beloning = cijferPunt * tcijfers
print(beloning)

#een string met een tekstuele omschrijving het gemiddelde en de beloning
overzicht = 'Mijn cijfers (gemiddeld ' + str(gemiddelde) + ' ) leveren een beloning van € ' + str(beloning) + ' op!'
print(overzicht)