def convert(temp_cel):
    temp_fahr = temp_cel * 1.8 + 32
    return temp_fahr

def table(begin_reeks, einde_reeks):
    for waarde in range(begin_reeks, einde_reeks):
        verander_waarde = convert(waarde)
        print("{} {}" .format(verander_waarde, waarde))


temp_cel_begin = eval(input('Vul het begin temperatuur in celcius: '))
tem_cel_einde = eval(input('Vul het eind temperatuur in celcius: '))

antwoord = table(temp_cel_begin, tem_cel_einde)
