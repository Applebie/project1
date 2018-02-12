import urllib
from xml.etree.ElementTree import parse
candidates =['1785','1394']
daves_lat = 41.980262
def distance(lat1,lat2):
    return 69*abs(lat1-lat2)

def monitor():
    u  = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid= bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, daves_lat)
            print busid, dis, 'miles'

import time
while True:
    monitor()
    time.sleep(60)
