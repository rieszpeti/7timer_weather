import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from timer_astro import structurizeData
from calculations import apparentTemp
import warnings
warnings.filterwarnings("ignore")

# Give insight to the data with visualization.

df, dfs = structurizeData()
df = pd.DataFrame(df)
df = df.reset_index()

# -------------------------------------------------------
# shows the apparent temperature and the mean of the temp
def apparentTempAndAvg():
    fig1, ax1 = plt.subplots(1)

    ax2 = ax1.twinx()
    ax1.bar(df['index'].unique(), df['temp2m', 'mean'], color='r')
    ax2.plot(df['index'].unique(), apparentTemp(df), 'b-')

    #ax1.set_xlabel('Cities')
    ax1.set_ylabel('Temp 2m C°', color='r')
    ax2.set_ylabel('Apparent Temp C°', color='b')
    ax1.set_xticklabels(df['index'].unique(), rotation='horizontal', size=8)
    plt.title("Feels like temperature vs actual temperature")

# -------------------------------------------------------
# shows the std of the cloud cover and the seeing
def cloudCoverSeeing():
    x = np.arange(len(df['index']))  # the label locations
    width = 0.35  # the width of the bars

    fig2, ax2 = plt.subplots(1)
    rects1 = ax2.bar(x - width / 2, df['cloudcover', 'mean'], width, yerr=df['cloudcover', 'std'], label='Cloud cover %')
    rects2 = ax2.bar(x + width / 2, df['seeing', 'mean'], width, yerr=df['seeing', 'std'], label='Seeing %')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax2.set_ylabel('Means of cloud cover and seeing')
    ax2.set_title('Std of Cloud cover and Seeing')
    ax2.set_xticks(x, df['index'])
    ax2.legend()

    ax2.bar_label(rects1, padding=3)
    ax2.bar_label(rects2, padding=3)

    fig2.tight_layout()

# -------------------------------------------------------
# shows the timepoints and the wind speed also the direction of the wind
def budapestWindAndDirection(dfs):
    dfs = dfs.drop('wind10m', axis=1)
    budapestDatas = pd.DataFrame(dfs.loc[dfs['city'] == 'Budapest'])

    # print(budapestDatas)

    x = budapestDatas['timepoint']
    y = budapestDatas['winddirection']
    c = budapestDatas['windspeed']

    fig3, ax3 = plt.subplots(1)
    plt.scatter(x, y, s=200, c=c)
    plt.colorbar().set_label("Windspeed m/s")

    plt.title("Budapest Wind Speed and Direction")
    plt.xlabel("Time point Hrs")
    plt.ylabel("Direction")

    plt.show()
