clc;clear;close all
format compact

eventFile = fileread("data/full_route_blue/events.json");
events = jsondecode(eventFile).events;

segemntFile = fileread("data/full_route_blue/disengagment_info.json");
segmentData = jsondecode(segemntFile);
segmentData.distance_totals

event_length = length(events);

% total_traveled = segmentData.distance_totals.total_travel_distance_m * 0.000621371

% Assuming eventLocations is a struct with 'events' field
x = zeros(1,event_length);
y = zeros(1,event_length);
c = zeros(event_length,3);
s = zeros(1,event_length);

f = waitbar(0, 'Extracting GNSS and Driving Modes...');
for i = 1:event_length
    item = events(i);
    gps = item.gps;
    if strcmp(item.can.drivingMode, 'COMPLETE_AUTO_DRIVE')
        color = [0 1 0];
        size = 10;
    elseif strcmp(item.can.drivingMode, 'EMERGENCY_MODE')
        color = [1 0 1];
        size = 10;
    else
        color = [1 0 0];
        size = 10;
    end
    x(i) = gps.latitude;
    y(i) = gps.longitude;
    c(i,:) = color;
    s(i) = size;

    waitbar(i/event_length, f)
end
close(f)

geobasemap streets
hold on
for i = 1:numel(segmentData.transition_info)
    lat = segmentData.transition_info(i).latitude;
    lon = segmentData.transition_info(i).longitude;
    geoscatter(lat, lon, 500, [0.9290 0.6940 0.1250], 'pentagram','filled')
    text(lat+0.00005, lon+0.00005, num2str(segmentData.transition_info(i).distance,4))
end
geoscatter(x,y,s,c,'filled')
% grid on
