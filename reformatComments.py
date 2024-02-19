import json
import os
from datetime import datetime

from glob import glob
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

def extractHMS(string, tz_offset):
    try:
        hour   = int(string[:2]) - int(tz_offset.seconds/3600)
        minute = int(string[2:4])
        second = int(string[4:6])
    except:
        hour = int(string[:2]) - int(tz_offset.seconds/3600)
        minute = int(string[3:5])
        second = int(string[6:8])
    return hour, minute, second

def fast_scandir(dirname):
    res = os.listdir(dirname)
    return res


ouPacifica = "/home/tmoleski_linux/s3bucket/Deployment_2_SEOhio/Blue Route/OU Pacifica/" 
# ouPacifica = "/media/travis/moleski2/cyber_bags/data/"
newDir    = "./commentCheck/"
newDir    = ouPacifica

subdirs = fast_scandir(ouPacifica)
print(subdirs)

for subdir in subdirs:
    print(subdir)

    subdir = int(subdir)
    directory = ouPacifica + str(subdir) + '/'

    str_from_time = datetime.utcfromtimestamp(subdir)

    tz_offset = str_from_time - datetime.fromtimestamp(subdir)

    print(directory, str_from_time, tz_offset)

    year = str_from_time.year
    month = str_from_time.month
    day = str_from_time.day

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        if os.path.isfile(f) and f.endswith(".txt") and 'groupid' or 'groupID' in filename:
            of = open(f, "r")
            content = of.read()
            groupID = content

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        masterDict ={
            'comments':[]
        }
        # if os.path.isfile(f) and f.endswith(".json") and re.match(r'[A-Za-z]', filename[0]):
        if os.path.isfile(f) and f.endswith(".json") and 'VanDrive_Comments' in filename:
        # if os.path.isfile(f) and f.endswith(".json")
            with open(f) as file:
                print(f)
                old = json.load(file)

                # print(f)

                for entry in old['comments']:
                    current_dict = {"header": {},
                                    "event": None,
                                    "position": None,
                                    }

                    if 'problem' in entry:
                        event = entry['problem']
                    else:
                        event = entry['comment']


                    data = entry['data']
                    time = data[0]

                    h,m,s = extractHMS(time, tz_offset)
                    epoch_time = int(datetime(year,month,day,h,m,s).strftime('%s'))

                    current_dict['header']['timestampSec']  = epoch_time
                    current_dict['event'] = event
                    current_dict['groupID'] = groupID

                    lat, lon, alt = getLatLonComments(entry)

                    LLH = {
                        'latitude': lat,
                        'longitude': lon,
                        'alt_msl': alt
                    }

                    current_dict['position'] = LLH

                    masterDict['comments'].append(current_dict)

                print(masterDict)

            save_dir = newDir + str(subdir) + "/comments.json"
            with open(save_dir, 'w') as fp:
                print("CREATED NEW FILE: ", save_dir)
                json.dump(masterDict, fp, indent=4)

