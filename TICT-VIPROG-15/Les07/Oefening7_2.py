#dictionary
'''''
Voor de dubbele punt: key
Na de dubbele punt: value
'''
week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do': 'donderdag', 'vr': 'vrijdag'}
#week['di'] = 'dinsdag'
#week['za'] = 'zaterdag'
#print(week['za'])

#keys printen
#for afkorting in week.keys():
#    print(afkorting)
#values printen
#for langeNaam in week.values():
#   print(langeNaam)

#beide afdrukken
#for beide in week.items():
#    print(beide)
#items afdrukken:
for afkorting in week.keys():
    print(afkorting, week[afkorting])
#In combinatie met formatmethode kun je je uitvoer aan eisen/wensen aanpassen bijv:
for afkorting in week:
    print('Afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))