import pickle    
import os
import json
from tqdm import tqdm
import numpy as np
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import TabPanel, ColumnDataSource, DataTable, TableColumn, Label, Tabs
import math
import argparse

class gnss_converter():
    def __init__(self):
        self.R = 6378137.0

    def merc_y(self, lat):
        return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)) * self.R

    def merc_x(self, lon):
        return math.radians(lon) * self.R

class bokeh_handler():
    def __init__(self, mercator_x, mercator_y, s, c, segments, travel_distances, filename, html_name):

        self.html_file_name = filename
        self.html_name = html_name
        
        output_file(filename=self.html_file_name, title=self.html_name)
    
        self.bound_ext = 200
        self.meter2mile = 0.000621371
        self.mercator_x = mercator_x
        self.mercator_y = mercator_y
        self.c = c
        self.s = s
        self.segments = segments
        self.travel_distances = travel_distances
        self.map_graph = figure(sizing_mode='scale_both',
                tools="pan,wheel_zoom,box_zoom,reset, fullscreen, copy, undo, redo, save",
                x_axis_type="mercator", y_axis_type="mercator", 
                x_range=(np.min(self.mercator_x)-self.bound_ext, np.max(self.mercator_x)+self.bound_ext), 
                y_range=(np.min(self.mercator_y)-self.bound_ext, np.max(self.mercator_y)+self.bound_ext),
                x_axis_label='Longitude',
                y_axis_label='Latitude'
                )
        self.map_graph.add_tile('CARTODBPOSITRON_RETINA')
        # self.map_graph.add_tile('OSM')

    def addSegments2Map(self):
        for segment in self.segments:
            segment['merc_x'] = merc_convert.merc_x(segment['longitude'])
            segment['merc_y'] = merc_convert.merc_y(segment['latitude'])

            self.map_graph.scatter(segment['merc_x'],segment['merc_y'] ,color='gold',marker='star', size=10, fill_alpha=0.5)

            dis = Label( x=segment['merc_x'],y=segment['merc_y'], text=str(round(segment['distance']*self.meter2mile,2))+ " mi", 
                        text_font = "arial",
                        text_font_size="6pt",
                        text_font_style = 'bold italic')

            self.map_graph.add_layout(dis)

    def addDrivingData2Map(self):
        self.map_graph.scatter(self.mercator_x, self.mercator_y, size=self.s, color=self.c, fill_alpha=0.5)

    def make_legend(self):
        self.map_graph.scatter(self.mercator_x[0],self.mercator_y[0], color='magenta', marker='triangle',size=10, legend_label='Start')
        self.map_graph.scatter(self.mercator_x[-1],self.mercator_y[-1], color='cyan', marker='square', size=10,  legend_label='End')
        self.map_graph.scatter([None],[None], color='green', marker='circle', size=10, legend_label='Auto')
        self.map_graph.scatter([None],[None], color='purple', marker='circle', size=10, legend_label='Emergency')
        self.map_graph.scatter([None],[None], color='red', marker='circle', size=10, legend_label='Manual')
        self.map_graph.scatter([None],[None], color='gold', marker='star', size=10, legend_label='Takeover')
        self.map_graph.legend
        self.map_graph.legend.border_line_alpha = 1
        self.map_graph.legend.border_line_color = 'black'
        self.map_graph.legend.background_fill_alpha = 0.2

    def make_table(self):
        table_dict = {
            "Names": [],
            "Values": []
        }
        for val in self.travel_distances:
            table_dict['Names'].append(val.split('_')[0])
            table_dict['Values'].append(travel_distances[val]*self.meter2mile)

        self.columns = [
            TableColumn(field='Names', title='Mode'),
            TableColumn(field='Values', title='Distance Traveled (miles)')
        ]
        self.data_table = DataTable(source=ColumnDataSource(table_dict), columns=self.columns)

    def make_tabs(self):
        self.map_tab   = TabPanel(child=self.map_graph, title="Map")
        self.table_tab = TabPanel(child=self.data_table, title='Distances')

        self.tabs = [self.map_tab, self.table_tab]

    def show_tabs(self):
        show(Tabs(tabs=self.tabs))
    
    def save_tabs(self):
        save(Tabs(tabs=self.tabs))

def extract_merc_drive_data(converter, events):
    x=[]
    y=[]
    c=[]
    s=[]
    lon = []
    lat = []
    mercator_x = []
    mercator_y = []
    for item in tqdm(events):
        if(item['can']['drivingMode'] == 'COMPLETE_AUTO_DRIVE'):
            color = 'green'
            size = 1
        elif(item['can']['drivingMode'] == 'EMERGENCY_MODE'):
            color = 'purple'
            size = 1
        else:
            color = 'red'
            size = 1
        x.append(float(item['gps']['x']))
        y.append(float(item['gps']['y']))
        c.append(color)
        s.append(float(size))
        lon.append(float(item['gps']['longitude']))
        lat.append(float(item['gps']['latitude']))
        mercX = converter.merc_x(float(item['gps']['longitude']))
        mercY = converter.merc_y(float(item['gps']['latitude']))
        mercator_x.append(mercX)
        mercator_y.append(mercY)

    return x,y,c,s,lon,lat,mercator_x,mercator_y

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Import info')

    parser.add_argument('--dataroot',  help='WHERE ARE THE PICKLES?')
    parser.add_argument('--html_root', help='WHERE YOU WANT FIG?')
    parser.add_argument('--show', action="store_true", help='Show fig?')

    args = parser.parse_args()

    data_root = args.dataroot
    html_root = args.html_root

    merc_convert = gnss_converter()

    filename = os.path.join(html_root, "html_fig.html")
    html_name = "Experiment Results"

    events_dat = os.path.join(data_root, "events.pkl")

    events   = pickle.load(open(events_dat,'rb'))['events']
    disengagment_dat = os.path.join(data_root, 'disengagement_info.json')

    with open(disengagment_dat, 'r') as f:
        disengagments = json.load(open(disengagment_dat))

    travel_distances = disengagments['distance_totals']
    segments = disengagments['transition_info']

    x,y,c,s,lon,lat,mercator_x,mercator_y = extract_merc_drive_data(merc_convert, events)

    plot_handler = bokeh_handler(mercator_x, mercator_y, s, c, segments, travel_distances, filename, html_name)
    plot_handler.addDrivingData2Map()
    plot_handler.addSegments2Map()
    plot_handler.make_legend()
    plot_handler.make_table()
    plot_handler.make_tabs()

    if args.show:
        plot_handler.show_tabs()
    else:
        plot_handler.save_tabs()
    



