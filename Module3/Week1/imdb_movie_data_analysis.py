
import pandas as pd

dataset_path = 'IMDB-Movie-Data.csv'

# Read data from .csv file
data = pd.read_csv(dataset_path)

# Read data with specified explicit index.
data_indexed = pd.read_csv(dataset_path, index_col="Title")

# Preview top 5 rows using head()
data.head()

# Preview last 5 rows using tail()
data.tail()

#  understand the basic information about this data
data.info()

data.describe()

# Data Selection – Indexing and Slicing data

# Extract data as Series

genre = data['Genre']

# Extract data as DataFrame (1 column)

genre = data[['Genre']]

# Extract data as DataFrame with some columns

columns = data[['Title','Genre','Actors','Director','Rating']]

data.set_index('Title')

# extract rows by specified Title Name

data.set_index('Title').loc[['Suicide Squad']]

# Slicing some rows by range of index with specified columns

data.iloc[10:15][['Title','Rating','Revenue (Millions)']]

# Data Selection – Based on Conditional filtering

data[((data['Year'] >= 2010) & (data['Year'] <= 2015))
      & (data['Rating'] < 6.0)
      & (data['Revenue (Millions)'] > data['Revenue (Millions)'].quantile(0.95))]

# Groupby Operations:

data[['Director', 'Rating']]

data.groupby('Director')[['Rating']].mean()

data.groupby('Director')[['Rating']].mean().head()

# Sorting Operations

x = data.groupby('Director')[['Rating']].mean()
x.sort_values(['Rating'], ascending=False).head()

# Dealing with missing values
# To check null values row-wise

data.isnull()

# total number of null values ​​in each column of the data table
data.isnull().sum()

data[data.isnull().any(axis=1)].head()

data.dropna().shape

# delete row
data.dropna()

# filling value
data.fillna(300).shape

data_indexed.fillna(300).shape

data_indexed['Revenue (Millions)'].fillna(300)

revenue_mean = data_indexed['Revenue (Millions)'].mean()
print ("The mean revenue is: ", revenue_mean )

# filling the null values with this mean revenue
data_indexed['Revenue (Millions)'].fillna(revenue_mean)

data.info()

# Use drop function to drop columns
data.drop(['Revenue (Millions)', 'Metascore'], axis=1).info()

# apply() functions

# Classify movies based on ratings
def rating_group(rating):
    if rating >= 7.5:
        return 'Good'
    elif rating >= 6.0:
        return 'Average'
    else:
        return 'Bad'

# Lets apply this function on our movies data
# creating a new variable in the dataset to hold the rating category
data['Rating_category'] = data['Rating'].apply(rating_group)

data[['Title','Director','Rating','Rating_category']].head(10)