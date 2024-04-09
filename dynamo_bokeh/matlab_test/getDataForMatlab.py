import pickle    
import os
import json

# from bokeh.plotting import figure, output_file, show  
# graph = figure()  

data_root = "../data/full_route_blue/"

events_dat = os.path.join(data_root, "events.pkl")
events   = pickle.load(open(events_dat,'rb'))['events']

disengagment_dat = os.path.join(data_root, 'disengagement_info.json')
with open(disengagment_dat, 'r') as f:
    disengagments = json.load(open(disengagment_dat))

travel_distances = disengagments['distance_totals']
segments = disengagments['transition_info']

x=[]
y=[]
c=[]
s=[]
for item in events:
    gps = item['gps']
    if(item['can']['drivingMode'] == 'COMPLETE_AUTO_DRIVE'):
        color = [0, 1, 0]
        size = 10
    elif(item['can']['drivingMode'] == 'EMERGENCY_MODE'):
        color = [1, 0, 1]
        size = 10
    else:
        color = [1, 0, 0]
        size = 10
    x.append(float(item['gps']['latitude']))
    y.append(float(item['gps']['longitude']))
    c.append(color)
    s.append(float(size))

# graph.scatter(x,y,c)

# show(graph)
