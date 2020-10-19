import json
import argparse

## argument handling
parser = argparse.ArgumentParser()
parser.add_argument('path')
args = parser.parse_args()


points = []
neighborhoods = []

with open(args.path) as f:
    data = json.load(f)
for feature in data['features']:
    properties = feature['properties']
    geometry = feature['geometry']
    lat_sum = 0
    long_sum = 0
    if(geometry['type'] == 'MultiPolygon'):
        first_section = geometry['coordinates'][0][0]
    else:
        first_section = geometry['coordinates'][0]
    for point in first_section:
        lat_sum += point[0]
        long_sum += point[1]
    neighborhoods.append((properties["Neighborhood_ID"], properties["Name"], properties["SqMiles"], lat_sum/len(first_section), long_sum/len(first_section)))
print(neighborhoods)
