#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20211015
#  desc: 
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import requests
from xml.etree import ElementTree
from datetime import datetime, timedelta

STATION_URL="https://tfl.gov.uk/tfl/syndication/feeds/stations.kml"
NS="{http://www.opengis.net/kml/2.2}"


for place in ElementTree.fromstring(requests.get(f"{STATION_URL}").content).findall(f"{NS}Document/{NS}Placemark"):
    print(place.find(f"{NS}name").text.strip())



#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
