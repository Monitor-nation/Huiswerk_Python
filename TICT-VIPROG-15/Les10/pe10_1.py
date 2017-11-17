import xmltodict

def processXML(filenaam):
    with open(filenaam) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary


artikelendict = processXML('artikelen.xml')
artikelen = artikelendict['artikelen']['artikel']

# filenaam = 'artikelen.xml'
for artikel in artikelen:
    print(artikel['naam'])

bestandsnaam = 'Bestand'
voorbeeldendict = 'artikelendict'
voorbeelden = 'artikel(en)'

rodeTag = ['artikelen']
groeneTag = ['arikel']
blauweTag = ['naam']