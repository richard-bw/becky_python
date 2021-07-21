#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210720
#  desc: 
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import requests
from datetime import datetime, timedelta

STATIONNAME     =   'West Barnes Level Crossing'
STOPPOINT_ID    =   '490014399N'

ARRIVALS_URL= f"https://api.tfl.gov.uk/StopPoint/{STOPPOINT_ID}/Arrivals"
arrivals = requests.get(ARRIVALS_URL).json()

print(f"Arrival times at {STATIONNAME} (time now: {datetime.now().strftime('%H:%M')})")
for arrival in sorted(arrivals, key=lambda k: k['timeToStation']):
    print (f"{arrival['lineName']} to {arrival['destinationName']} - due: {(datetime.now() + timedelta(seconds=arrival['timeToStation'])).strftime('%H:%M')}")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
