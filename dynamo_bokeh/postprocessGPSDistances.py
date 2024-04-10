import pickle
import matplotlib.pyplot as plt
import numpy as np
import utm
import json
import os

from tqdm import tqdm

def detect_transition(data):
    transitions = []
    for i in range(1, len(data)):
        if data[i - 1]['can']['drivingMode'] != data[i]['can']['drivingMode'] :
            transitions.append(i)  
    return transitions

def llh_to_xyz_dict(llh):
    xyzlist = []
    for pair in llh:
        xyz = llh_to_xyz(float(pair['latitude']), float(pair['latitude']), float(pair['heightMsl']))
        xyzlist.append(xyz)
    return xyzlist

def llh_to_xyz(latitude, longitude, altitude):
    res = utm.from_latlon(latitude=latitude, longitude=longitude)
    x, y, zone_number, zone_letter = res
    z = altitude
    return x, y, z
    
def segment_tracks(data, transitions):
    segments = []
    start_index = 0
    for i in transitions:
        segments.append(data[start_index:i])
        start_index = i
    segments.append(data[start_index:])
    return segments

def travel_distance(eventLocations):
    lastgps = None
    distance = 0
    for item in eventLocations:
        gps = item['gps']
        gps['x'], gps['y'], gps['z'] = llh_to_xyz(float(gps['latitude']), float(gps['longitude']), float(gps['heightMsl']))
        if(lastgps is not None):
            distance = distance + np.sqrt(
                        np.power(gps['x'] - lastgps['x'],2) + 
                        np.power(gps['y'] - lastgps['y'],2) + 
                        np.power(gps['z'] - lastgps['z'],2)
                        )
            lastgps = gps
        elif(lastgps == None):
            lastgps = gps
    return distance


def disengagement_distances(eventLocations):
    transition_indices = detect_transition(eventLocations)
    segments = segment_tracks(eventLocations, transition_indices)
    transitions = {
        'transition_info': []
    }
    for i, segment in enumerate(segments):
        mode_distance = {}
        mode_distance['distance'] = float(travel_distance(segment))
        mode_distance['segment_id'] = int(i)
        mode_distance['drive_mode'] = str(segment[i]['can']['drivingMode'])
        mode_distance['x'] = float(segment[i]['gps']['x'])
        mode_distance['y'] = float(segment[i]['gps']['y'])
        mode_distance['gps_time'] = float(segment[i]['gps']['header']['timestampSec'])
        mode_distance['can_time'] = float(segment[i]['can']['header']['timestampSec'])
        transitions['transition_info'].append(mode_distance)
    return transitions, transition_indices


if __name__ == "__main__":
    data_root = "./data/full_route_blue/"

    canbus_dat = os.path.join(data_root, "canbus.pkl")
    gps_dat    = os.path.join(data_root, "gpsloc.pkl")

    canbus_chassis = pickle.load(open(canbus_dat,'rb'))
    GPSLocations   = pickle.load(open(gps_dat,'rb'))

    print("Sorting...")

    canbus_chassis.sort(key=lambda x:x['header']['timestampSec'])
    GPSLocations.sort(key=lambda x:x['header']['timestampSec'])

    print(f"CAN # {len(canbus_chassis)}")
    print(f"GPS # {len(GPSLocations)}")

    eventLocations = []
    count = 0
    tempSave = 0
    for can in tqdm(canbus_chassis):
        time_to_find = can['time']
        gpsfound = None
        for gps in GPSLocations:
            if(gps['time'] >= time_to_find):
                gpsfound = gps
                break
        if(gpsfound is not None):
            # print(f"Found gps {can['time']} / {gpsfound['time']} {gpsfound['longitude']} {gpsfound['latitude']} {gpsfound['x']} {gpsfound['y']} {count}")
            eventLocations.append({'can':can,'gps':gpsfound})
            count = count + 1
            tempSave += 1
            if tempSave > 1000:
                # print("DUMPED...")
                pickle.dump(eventLocations,open(data_root+'events.pkl','wb'))
                tempSave = 0
                # break
        else:
                print(f"Missing {can['time']}")
    print(f"Found {count} pairs")
    pickle.dump(eventLocations,open(data_root+'events.pkl','wb'))
    print("DUMPED TO ", data_root+'events.pkl')

    eventLocations = pickle.load(open(data_root+'events.pkl','rb'))
    x=[]
    y=[]
    c=[]
    s=[]
    for item in eventLocations:
        gps = item['gps']
        gps['x'], gps['y'], gps['z'] = llh_to_xyz(float(gps['latitude']), float(gps['longitude']), float(gps['heightMsl']))
        if(item['can']['drivingMode'] == 'COMPLETE_AUTO_DRIVE'):
            color = 'green'
            size = 50
        elif(item['can']['drivingMode'] == 'EMERGENCY_MODE'):
            color = 'purple'
            size = 50
        else:
            color = 'red'
            size = 100
        x.append(item['gps']['x'])
        y.append(item['gps']['y'])
        c.append(color)
        s.append(size)

    total_travel_distance   = travel_distance(eventLocations)
    segments, transition_indices = disengagement_distances(eventLocations)

    total_auto_dist = 0
    total_man_dist  = 0
    total_emergency_dist = 0
    for i in range(len(segments['transition_info'])):
        dat = segments['transition_info'][i]

        if dat['drive_mode'] == 'COMPLETE_AUTO_DRIVE':
            total_auto_dist += dat['distance']

        elif dat['drive_mode'] == 'EMERGENCY_MODE':
            total_emergency_dist += dat['distance']

        else:
            total_man_dist += dat['distance']

    tot_check = total_auto_dist + total_man_dist + total_emergency_dist
    print("TRAVEL DISTANCE (miles): ", total_travel_distance* 0.000621371)
    print("MANUAL DISTANCE (miles): ",  total_man_dist* 0.000621371)
    print("AUTO DISTANCE   (miles): ", total_auto_dist* 0.000621371)
    print("EMERGENCY DISTANCE (miles)", total_emergency_dist*0.000621371)
    print("CHECKED SUM OF DISTANCE",    tot_check * 0.000621371)

    segments['distance_totals'] = {
        'manual_distance_m': total_man_dist,
        'auto_distance_m': total_auto_dist,
        'emergency_distance_m': total_emergency_dist,
        'total_travel_distance_m': total_travel_distance
    }

    fname= data_root+"disengagment_info.json"
    with open(fname,'w') as f:
        json.dump(segments, f, indent=4)
        f.close()
    print("DUMPED TO ", fname)

    for i in range(len(segments['transition_info'])):
        dat = segments['transition_info'][i]
        plt.scatter(dat['x'], dat['y'], marker='*',s=500, color='gold')
        plt.text(dat['x']-10, dat['y']-10, round(dat['distance'] * 0.000621371, 2))

    plt.scatter(x, y, color=c,s=s)
    plt.grid(True)
    plt.axis('Equal')
    plt.xlabel("X UTM (m)")
    plt.ylabel("Y UTM (m)")
    plt.show()