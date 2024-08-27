import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset_path = './opsd_germany_daily.csv'

# Read data from .csv file
opsd_daily = pd.read_csv(dataset_path)

print(opsd_daily.shape)
print(opsd_daily.dtypes)
opsd_daily.head(3)

# select Date column as index, because this column value in the data set is always unique
opsd_daily = opsd_daily.set_index('Date')
opsd_daily.head(3)

opsd_daily = pd.read_csv(dataset_path, index_col=0, parse_dates=True)

# Add columns with year , month , and weekday name
opsd_daily['Year'] = opsd_daily.index.year
opsd_daily['Month'] = opsd_daily.index.month
opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

# Display a random sampling of 5 rows
opsd_daily.sample(5, random_state=0)

# Time-based indexing
# access data over a period of time

opsd_daily.loc['2014-01-20':'2014-01-25']

# partial-string indexing, which allows us to slice by time description in a general way

new_opsd_df = opsd_daily.loc['2012-02']
new_opsd_df.head()

# Visualizing time series data
# Data graph of daily electricity consumption in Germany

sns.set(rc={'figure.figsize':(11, 4)})
col_to_plot = 'Consumption'
opsd_daily[col_to_plot].plot(linewidth=0.5)
plt.ylabel(col_to_plot)
plt.show()

# Data graph of solar power output
col_to_plot = 'Solar'
opsd_daily[col_to_plot].plot(linewidth=0.5, color='orange')
plt.ylabel(col_to_plot)
plt.show()

# Data graph of solar power output
sns.set(rc={'figure.figsize':(11, 4)})
col_to_plot = 'Wind'
opsd_daily[col_to_plot].plot(linewidth=0.5, color='green')
plt.ylabel(col_to_plot)
plt.show()

cols_plot = ['Consumption', 'Solar', 'Wind']
axes = opsd_daily[cols_plot].plot(
    marker='.',
    alpha=0.5,
    linestyle='None',
    figsize=(11, 9),
    subplots=True
)
for ax in axes:
    ax.set_ylabel('Daily Totals (GWh)')

plt.show()

# Seasonality: An index of characteristics that repeat over a fixed period of time across years.

fig, axes = plt.subplots(3, 1, figsize=(11, 10), sharex=True)
for name, ax in zip(['Consumption', 'Solar', 'Wind'], axes):
    sns.boxplot(data=opsd_daily, x='Month', y=name, ax=ax)
    ax.set_ylabel('GWh')
    ax.set_title(name)
    # Remove the automatic x-axis label from all but the bottom subplot
    if ax != axes[-1]:
        ax.set_xlabel('')

# get frequency by day
pd.date_range('1998-03-10', '1998-03-15', freq='D')

pd.date_range('2004-09-20', periods=8, freq='h')

# To select an arbitrary sequence of date/time values from a pandas time series,
# we need to use a DatetimeIndex, rather than simply a list of date/time strings
times_sample = pd.to_datetime(['2013-02-03', '2013-02-06', '2013-02-08'])
# Select the specified dates and just the Consumption column
consum_sample = opsd_daily.loc[times_sample, ['Consumption']].copy()

# Convert the data to daily frequency, without filling any missings
consum_freq = consum_sample.asfreq('D')
# Create a column with missings forward filled
consum_freq['Consumption - Forward Fill'] = consum_sample.asfreq('D', method='ffill')

# Resampling: change the sampling frequency of the time series data set

data_columns = ['Consumption', 'Wind', 'Solar', 'Wind+Solar']
# Resample downsampling from daily to weekly frequency , aggregating with mean
opsd_weekly_mean = opsd_daily[data_columns].resample('W').mean()
opsd_weekly_mean.head(3)

# The number of data samples by weekly will be less than the daily original table and 1/7 times less.
print(opsd_daily.shape[0])
print(opsd_weekly_mean.shape[0])

# visualize daily and weekly time series of Solar for 6 months

# Start and end of the date range to extract
start, end = '2017-01', '2017-06'
# Plot daily and weekly resampled time series together
fig, ax = plt.subplots()
ax.plot(opsd_daily.loc[start:end, 'Solar'],
marker='.', linestyle='-', linewidth=0.5, label='Daily')
ax.plot(opsd_weekly_mean.loc[start:end, 'Solar'],
marker='o', markersize=8, linestyle='-', label='Weekly Mean Resample')
ax.set_ylabel('Solar Production (GWh)')
ax.legend()
plt.show()

# Compute the annual sums, setting the value to NaN for any year which has
# fewer than 360 days of data
opsd_annual = opsd_daily[data_columns].resample('YE').sum(min_count=360)
# The default index of the resampled DataFrame is the last day of each year,
# ('2006-12-31', '2007-12-31', etc.) so to make life easier, set the index
# to the year component
opsd_annual = opsd_annual.set_index(opsd_annual.index.year)
opsd_annual.index.name = 'Year'
# Compute the ratio of Wind+Solar to Consumption
opsd_annual['Wind+Solar/Consumption'] = opsd_annual['Wind+Solar'] / opsd_annual['Consumption']
opsd_annual.tail(3)

# Plot from 2012 onwards, because there is no solar production data in earlier years
ax = opsd_annual.loc[2012:, 'Wind+Solar/Consumption'].plot.bar(color='C0')
ax.set_ylabel('Fraction')
ax.set_ylim(0, 0.3)
ax.set_title('Wind + Solar Share of Annual Electricity Consumption')
plt.xticks(rotation=0)
plt.show()

"""## 8. Rolling windows"""

# Rolling windows

opsd_daily[data_columns].head(8)

# Compute the centered 7-day rolling mean
opsd_7d = opsd_daily[data_columns].rolling(7, center=True).mean()
opsd_7d.head(8)

# Trends: a feature that indicates the direction of the data

import matplotlib.dates as mdates

# The min_periods=360 argument accounts for a few isolated missing days in the
# wind and solar production time series
opsd_365d = opsd_daily[data_columns].rolling(
    window=365,
    center=True,
    min_periods=360
).mean()

# Plot daily, 7-day rolling mean, and 365-day rolling mean time series
fig, ax = plt.subplots()
ax.plot(opsd_daily['Consumption'], marker='.', markersize=2, color='0.6',
linestyle='None', label='Daily')
ax.plot(opsd_7d['Consumption'], linewidth=2, label='7-d Rolling Mean')
ax.plot(opsd_365d['Consumption'], color='0.2', linewidth=3,
label='Trend (365-d Rolling Mean)')
# Set x-ticks to yearly interval and add legend and labels
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Consumption (GWh)')
ax.set_title('Trends in Electricity Consumption')
plt.show()

# Plot 365-day rolling mean time series of wind and solar power
fig, ax = plt.subplots()
for nm in ['Wind', 'Solar', 'Wind+Solar']:
    ax.plot(opsd_365d[nm], label=nm)
    # Set x-ticks to yearly interval, adjust y-axis limits, add legend and labels
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.set_ylim(0, 400)
    ax.legend()
    ax.set_ylabel('Production (GWh)')
    ax.set_title('Trends in Electricity Production (365-d Rolling Means)')
plt.show()