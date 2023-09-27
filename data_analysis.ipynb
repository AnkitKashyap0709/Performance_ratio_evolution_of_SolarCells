import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import math as m
from matplotlib.lines import Line2D

df = pd.read_csv(r'/content/sample_data/Cleantech Solar.csv')
df['Date'] = pd.to_datetime(df['Date'], infer_datetime_format = True) # The date-time format is set to true for faster parsing inside the dataset

fig, ax = plt.subplots(figsize = (12, 8)) # The figsize parameter is used to specify the width and height of the figure in inches. In this case, the figure size is set to 12 inches by 8 inches.

conditions = [(df['GHI'] < 2),
              (df['GHI'] >= 2) & (df['GHI'] < 4),
              (df['GHI'] >= 4) & (df['GHI'] < 6),
              (df['GHI'] >= 6)]
colors = ['navy', 'cyan', 'orange', 'brown']
ax.scatter(df['Date'], df['PR'], c = np.select(conditions, colors), s = 5) # All the scatter points are plotted inside the graph and their individual colors are set according to GHI

rolling_mean = df['PR'].rolling(window = 30).mean()
a, = ax.plot(df['Date'], rolling_mean, color = 'red', linewidth = 2.2, label = '30-d moving average of PR') # Plot for the 30-d moving average of PR

ax.set_title('Performance Ratio Evolution (From 2019-07-01 to 2022-03-24)')
ax.set_xlabel('Date')
ax.set_ylabel('Performance Ratio [%]')

ax.set_ylim(ymin = 0)
ax.set_ylim(ymax = 100)
ax.set_yticks(range(0, 110, 10))
