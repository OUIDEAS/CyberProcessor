clc;clear;close all
format compact

[x, y, c, s, travel_distances, segments] = pyrunfile("getDataForMatlab.py", ["x", "y", "c", "s", "travel_distances", "segments"]);
travel_distances = struct(travel_distances)

m2mile = 0.000621371;

geobasemap streets
hold on

x = cell(x);
x = [x{:}];

y = cell(y);
y = [y{:}];

c = cell(c);
col = zeros(length(x),3);
for i = 1:length(c)
    temp_c = cell(c{i});
    temp_c = cellfun(@double,temp_c);
    col(i,:) = temp_c;
end
geoscatter(x, y, s, col,'filled')
for j = 1:length(segments)
    tempS = cell(segments(j));
    tempS = struct(tempS{:});
    lat = tempS.latitude;
    lon = tempS.longitude;
    geoscatter(lat, lon, 50, [0.9290 0.6940 0.1250], 'pentagram','filled')
    text(lat+0.00005, lon+0.00005, num2str(tempS.distance,4))
end

qw{1} = geoscatter(nan, nan, 50, [0.9290 0.6940 0.1250], 'pentagram','filled');
qw{2} = geoscatter(nan, nan, 50, 'r', 'filled');
qw{3} = geoscatter(nan, nan, 50, 'm', 'filled');
qw{4} = geoscatter(nan, nan, 50, 'g', 'filled');
qw{5} = geoscatter(x(1), y(1), 100, 'k', '^', 'filled');
qw{6} = geoscatter(x(end), y(end), 100, 'cyan', 'square','filled');
legend([qw{:}], {'Takeover','Manual','Emergency', 'Auto', 'Start', 'End'}, 'location', 'best')

