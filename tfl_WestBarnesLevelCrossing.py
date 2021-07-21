#!/usr/bin/env python3
#
#  auth: rbw
#  date: 20210720
#  desc: 
#  Bus stops in 5000m radius
# https://api.tfl.gov.uk/StopPoint/?lat=51.396163&lon=-0.2393173&stopTypes=NaptanPublicBusCoachTram&radius=5000
#
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import requests
from datetime import datetime, timedelta

STATIONNAME     =   'West Barnes Level Crossing'
                    #  "Stop E"    "Stop P"
STOPPOINT_IDS   =   ['490014399N', '490014399S'] 

print(f"Arrival times at {STATIONNAME} (time now: {datetime.now().strftime('%H:%M')})")
for stopPoint in STOPPOINT_IDS:
    arrivals = requests.get(f"https://api.tfl.gov.uk/StopPoint/{stopPoint}/Arrivals").json()
    for arrival in sorted(arrivals, key=lambda k: k['timeToStation']):
        print (f"{arrival['lineName']} to {arrival['destinationName']:30} - due: {(datetime.now() + timedelta(seconds=arrival['timeToStation'])).strftime('%H:%M')}")

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#//EOF
