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
    # print("processing ", city, "...")
    data = requests.get("https://www.7timer.info/bin/astro.php",
                        params=dict(lat=coord[0], lon=coord[1], unit='metric', output='json'))
    df = pd.DataFrame(data.json()['dataseries'])
    df.insert(loc=0, column='city', value=city)
    dfs_temp.append(df)
    # print(dfs)

# remove unnecessary headers and create new indexing
dfs = pd.concat(dfs_temp, ignore_index=True)

pd.set_option('display.expand_frame_repr', False)  # shows all the values

# --------------------------------------------------------------
# Use pandas to structure the data, e.g. by creating one big dataframe with a city column,
# and then applying group or pivot using the city name

windSplit = pd.json_normalize(dfs['wind10m'])  # splits the wind dictionary to two columns,
# because one of them is categorical and the other is numerical

categorical = pd.DataFrame(dfs['city'])  # add the categorical columns to the main df
categorical['direction'] = windSplit['direction']
categorical['prec_type'] = dfs['prec_type']

groupedCategorical = categorical.groupby('city').describe()

dfs['windspeed'] = windSplit['speed']  # add the new two columns to the dfs
dfs['winddirection'] = windSplit['direction']

# --------------------------------------------------------------
# Calculate basic statistics from all available data
# (numerical: min, max, mean, std; categorical: count, unique, top, freq)

numerical = dfs.groupby(
    'city').describe()  # get the analysis with the describe method this will only give the numerical value

analyzed_data = numerical.join(groupedCategorical)

total = []  # pass the analyzed data grouped by cities

for key in coordinates:
    # print(analyzed_data.loc[f'{key}'])
    total.append(analyzed_data.loc[f'{key}'])
