import requests
import pandas as pd

# http://www.7timer.info/doc.php?lang=en#astro

coordinates = {
    'Budapest': (47, 19),
    'London': (51, 0),
    'New York': (40, 73),
    'Tokyo': (35, 139),
    'Cape Town': (33, 18)
}


dfs_temp = []

for city, coord in coordinates.items():
    #print("processing ", city, "...")
    data = requests.get("https://www.7timer.info/bin/astro.php", params=dict(lat=coord[0], lon=coord[1], unit='metric', output='json'))
    df = pd.DataFrame(data.json()['dataseries'])
    df.insert(loc=0, column='city', value=city)
    dfs_temp.append(df)
    #print(dfs)

#remove unnecessary headers and create new indexing
dfs = pd.concat(dfs_temp, ignore_index=True)

#print(dfs)

#print(df.iloc[0])

#timepoint  cloudcover   seeing   transparency    lifted_index    rh2m    wind10m  temp2m prec_type
#                                                         wind10m {'direction': 'NW', 'speed': 3}

pd.set_option('display.expand_frame_repr', False)
#print(dfs.columns.values.tolist())
#print(dfs)
print('\n')

# Use pandas to structure the data, eg. by creating one big dataframe with a city column,
# and then applying groupby or pivot using the city name

#groupby the cities

#grouped = dfs.groupby('city').aggregate(lambda x: ','.join(map(str, x)))

#Calculate basic statistics from all available data (numerical: min, max, mean, std; categorical: count, unique, top, freq)

#print(grouped.take([0])['timepoint'])

windSplit = pd.json_normalize(dfs['wind10m'])

categorical = pd.DataFrame(dfs['city'])
categorical['direction'] = windSplit['direction']
categorical['prec_type'] = dfs['prec_type']

dfs['windspeed'] = windSplit['speed']

#dfs.pop('wind10m')
#dfs.pop('prec_type')
numerical = dfs.groupby('city').describe()

#print(numerical)
#dfs.groupby('city').apply(print)

groupedCategorical = categorical.groupby('city').describe()

analyzed_data = numerical.join(groupedCategorical)

print(analyzed_data)