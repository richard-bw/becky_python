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

word = "mackerel"

for place in ElementTree.fromstring(requests.get(f"{STATION_URL}").content).findall(f"{NS}Document/{NS}Placemark"):
    station_name = place.find(f"{NS}name").text.replace("Station", "").strip()
    match = False
    for cw in word:
        if match: break
        for cs in station_name:
            if (cw==cs): 
                match = True
                break
    if (not match ): print(station_name) 


#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
