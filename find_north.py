daves_lat = 41.98062
#daves_long = -87.668452

from xml.etree.ElementTree import parse
doc = parse('rt22.xml')

for bus in doc.findall('bus'):
    lat = float(bus.findtext('lat'))
    if lat > daves_lat:
        direction=bus.findtext('d')
        if direction.startswith('North'):
             busid = bus.findtext('id')
             print busid, lat

