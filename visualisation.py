import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from timer_astro import total, dfs
from calculations import apparentTemp
import warnings
warnings.filterwarnings("ignore")


# Give insight to the data with visualization.
# Be creative and pick a variety of plot types. Possible libraries: pandas builtin, plotly, matplotlib

df = pd.DataFrame(total)
df = df.reset_index()

# -------------------------------------------------------
# shows the apparent temperature and the mean of the temp
def apparentTempAndAvg():
    fig1, ax1 = plt.subplots(1)

    ax2 = ax1.twinx()
    ax1.bar(df['index'].unique(), df['temp2m', 'mean'])
    ax2.plot(df['index'].unique(), apparentTemp(df), 'b-')

    ax1.set_xlabel('Cities')
    ax1.set_ylabel('Temp 2m', color='g')
    ax2.set_ylabel('Apparent Temp', color='b')
    ax1.set_xticklabels(df['index'].unique(), rotation='vertical', size=8)

# -------------------------------------------------------
# shows the std of the cloud cover and the seeing
def cloudCoverSeeing():
    x = np.arange(len(df['index']))  # the label locations
    width = 0.35  # the width of the bars

    fig2, ax2 = plt.subplots(1)
    rects1 = ax2.bar(x - width / 2, df['cloudcover', 'mean'], width, yerr=df['cloudcover', 'std'], label='Cloud cover')
    rects2 = ax2.bar(x + width / 2, df['seeing', 'mean'], width, yerr=df['seeing', 'std'], label='Seeing')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax2.set_ylabel('Means')
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

    x = budapestDatas['winddirection']
    y = budapestDatas['timepoint']
    c = budapestDatas['windspeed']

    fig3, ax3 = plt.subplots(1)
    plt.scatter(x, y, s=200, c=c)
    plt.colorbar()

    plt.title("Budapest Wind Speed and Direction")
    plt.xlabel("Direction")
    plt.ylabel("Time point")

    plt.show()
