import json
import os
from datetime import datetime

import re

def dms_to_dd(d, m, s):
    if d[0]=='-':
        dd = float(d) - float(m)/60 - float(s)/3600
    else:
        dd = float(d) + float(m)/60 + float(s)/3600
    return dd

def nmeaGGA2decDeg(GGA):
    if int(GGA[0]) != 0:
        deg = GGA[0] + GGA[1]
        min = GGA[2:]
    else:
        deg = GGA[0] + GGA[1] + GGA[2]
        min = GGA[3:]
    decimal = dms_to_dd(deg,min,0)
    return(decimal)

def getLatLonComments(comment):
    lat = nmeaGGA2decDeg(comment['data'][1])
    
    lat_dir = comment['data'][2]

    if lat_dir == 'S':
        lat = lat * -1

    lon = nmeaGGA2decDeg(comment['data'][3])
    lon_dir = comment['data'][4]

    if lon_dir == 'W':
        lon = lon * -1

    alt = float(comment['data'][8])

    return lat, lon, alt

def extractHMS(string):
    try:
        hour   = int(string[:2]) - 5
        minute = int(string[2:4])
        second = int(string[4:6])
    except:
        hour = int(string[:2]) - 5
        minute = int(string[3:5])
        second = int(string[6:8])

            
    return hour, minute, second

subdir = 1705954227

directory = "/media/travis/moleski2/cyber_bags/" + str(1705954227) + '/'
newDir    = "/media/travis/moleski2/cyber_bags/" + str(1705954227) + '/'

str_from_time = datetime.fromtimestamp(subdir)

year = str_from_time.year
month = str_from_time.month
day = str_from_time.day

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f) and f.endswith(".txt") and 'groupID' in filename:
        of = open(f, "r")
        content = of.read()
        groupID = content

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    masterDict ={
        'comments':[]
    }
    if os.path.isfile(f) and f.endswith(".json") and re.match(r'[A-Za-z]', filename[0]):
    # if os.path.isfile(f) and f.endswith(".json")
        with open(f) as file:
            print(f)
            old = json.load(file)

            # print(f)

            for entry in old['comments']:
                current_dict = {}

                event = entry['problem']
                data = entry['data']
                time = data[0]

                h,m,s = extractHMS(time)
                epoch_time = float(datetime(year,month,day,h,m,s).strftime('%s'))

                current_dict['timestampSec']  = epoch_time
                current_dict['event'] = event
                current_dict['groupID'] = groupID

                lat, lon, alt = getLatLonComments(entry)

                LLH = {
                    'latitude': lat,
                    'longitude': lon,
                    'alt_msl': alt
                }

                current_dict['gnssPosition'] = LLH

                masterDict['comments'].append(current_dict)

            print(masterDict)

        with open(newDir+filename, 'w') as fp:
            print("CREATED NEW FILE: ", newDir+filename)
            json.dump(masterDict, fp, indent=4)

