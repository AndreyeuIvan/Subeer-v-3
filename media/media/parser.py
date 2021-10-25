import xmltodict

with open('map1.osm', 'r', encoding='utf-8') as f:
    xml = f.read()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])
