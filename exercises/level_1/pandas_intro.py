"""
https://pandas.pydata.org/pandas-docs/stable/getting_started/overview.html

pandas is a Python package providing fast, flexible, and expressive data structures
designed to make working with “relational” or “labeled” data both easy and intuitive.
It aims to be the fundamental high-level building block for doing practical,
real world data analysis in Python.
Additionally, it has the broader goal of becoming the most powerful
and flexible open source data analysis / manipulation tool available in any language.
It is already well on its way toward this goal.

pandas is well suited for many different kinds of data:
    Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet
    Ordered and unordered (not necessarily fixed-frequency) time series data.
    Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels
    Any other form of observational / statistical data sets. The data actually need not be labeled at all to be placed into a pandas data structure

The two primary data structures of pandas, Series (1-dimensional) and DataFrame (2-dimensional),
handle the vast majority of typical use cases in
finance, statistics, social science, and many areas of engineering.
For R users, DataFrame provides everything that R’s data.frame provides and much more.
pandas is built on top of NumPy and is intended to integrate well within
a scientific computing environment with many other 3rd party libraries.

Here are just a few of the things that pandas does well:
    Easy handling of missing data (represented as NaN) in floating point
    as well as non-floating point data

    Size mutability: columns can be inserted and deleted from
    DataFrame and higher dimensional objects

    Automatic and explicit data alignment: objects can be explicitly aligned to a set of labels,
    or the user can simply ignore the labels and let Series, DataFrame, etc.
    automatically align the data for you in computations

    Powerful, flexible group by functionality to perform split-apply-combine operations
    on data sets, for both aggregating and transforming data

    Make it easy to convert ragged, differently-indexed data in other Python
    and NumPy data structures into DataFrame objects

    Intelligent label-based slicing, fancy indexing, and subsetting of large data sets

    Intuitive merging and joining data sets

    Flexible reshaping and pivoting of data sets

    Hierarchical labeling of axes (possible to have multiple labels per tick)

    Robust IO tools for loading data from flat files (CSV and delimited),
    Excel files, databases, and saving / loading data from the ultrafast HDF5 format

    Time series-specific functionality: date range generation and frequency conversion,
    moving window statistics, moving window linear regressions, date shifting and lagging, etc.

Many of these principles are here to address the shortcomings frequently
experienced using other languages / scientific research environments.
For data scientists, working with data is typically divided into multiple stages:
munging and cleaning data, analyzing / modeling it, then organizing the results
of the analysis into a form suitable for plotting or tabular display.
pandas is the ideal tool for all of these tasks.

Some other notes
    pandas is fast. Many of the low-level algorithmic bits have been extensively tweaked
    in Cython code. However, as with anything else generalization usually sacrifices performance.
    So if you focus on one feature for your application you may be able
    to create a faster specialized tool.

    pandas is a dependency of statsmodels, making it an important part of
    the statistical computing ecosystem in Python.

    pandas has been used extensively in production in financial applications.


Data Structures
Dimensions	  Name	       Description
    1	     Series	     1D labeled homogeneously-typed array
    2	    DataFrame	 General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column

Why more than one data structure?

The best way to think about the pandas data structures is as flexible containers
for lower dimensional data. For example, DataFrame is a container for Series,
and Series is a container for scalars. We would like to be able to insert and remove
objects from these containers in a dictionary-like fashion.

Also, we would like sensible default behaviors for the common API functions which take
into account the typical orientation of time series and cross-sectional data sets.
When using ndarrays to store 2- and 3-dimensional data, a burden is placed on the user
to consider the orientation of the data set when writing functions;
axes are considered more or less equivalent
(except when C- or Fortran-contiguousness matters for performance).
In pandas, the axes are intended to lend more semantic meaning to the data;
i.e., for a particular data set there is likely to be a “right” way to orient the data.
The goal, then, is to reduce the amount of mental effort required to code up data
transformations in downstream functions.

For example, with tabular data (DataFrame) it is more semantically helpful to think of the index
(the rows) and the columns rather than axis 0 and axis 1.
Iterating through the columns of the DataFrame thus results in more readable code:
for col in df.columns:
    series = df[col]
    # do something with series

Mutability and copying of data

All pandas data structures are value-mutable
(the values they contain can be altered) but not always size-mutable.
The length of a Series cannot be changed, but, for example, columns
can be inserted into a DataFrame. However, the vast majority of methods produce new objects
and leave the input data untouched. In general we like to favor immutability where sensible.
"""

import numpy as np
import pandas as pd

# Object Creation

# Creating a Series by passing a list of values, letting pandas create a default integer index
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Creating a DataFrame by passing a NumPy array, with a datetime index and labeled columns
dates = pd.date_range('20130101', periods=6)
print(dates)

# Creating a DataFrame by passing a dict of objects that can be converted to series-like
df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})
print(df2)

# The columns of the resulting DataFrame have different dtypes
try:
    print(df2.types)
except AttributeError:
    pass

# Viewing Data

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])

print(df.head())
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.to_numpy())
print(df2.to_numpy())
print(df.describe())
print(df.T)  # Transposing your data
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by='B'))
print(df['A'])
print(df[0:3])
print(df['20130102':'20130104'])
# print(df.loc[dates[0]])
print(df.loc[:, ['A', 'B']])  # Selecting on a multi-axis by label
print(df.loc['20130102':'20130104', ['A', 'B']])  # Showing label slicing, both endpoints are included
# print(df.loc['20130102', ['A', 'B']])  # Reduction in the dimensions of the returned object
# print(df.loc[dates[0], 'A'])  # For getting a scalar value
# print(df.at[dates[0], 'A'])  # For getting fast access to a scalar (equivalent to the prior method)

# Selection by Position

# Select via the position of the passed integers
print(df.iloc[3])

# By integer slices, acting similar to numpy/python
print(df.iloc[3:5, 0:2])

# By lists of integer position locations, similar to the numpy/python style
print(df.iloc[[1, 2, 4], [0, 2]])

# For slicing rows explicitly
print(df.iloc[1:3, :])

# For slicing columns explicitly
print(df.iloc[:, 1:3])

# For getting a value explicitly
print(df.iloc[1, 1])

# For getting fast access to a scalar (equivalent to the prior method)
print(df.iat[1, 1])

# Boolean Indexing

# Using a single column’s values to select data.
print(df[df.A > 0])

# Selecting values from a DataFrame where a boolean condition is met
print(df[df > 0])

# Using the isin() method for filtering
df2 = df.copy()
# df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
# print(df2[df2['E'].isin(['two', 'four'])])


# Setting

# Setting a new column automatically aligns the data by the indexes
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
print(s1)

# Setting values by label
df.at[dates[0], 'A'] = 0

# Setting values by position:
df.iat[0, 1] = 0

# Setting by assigning with a NumPy array:
df.loc[:, 'D'] = np.array([5] * len(df))

# The result of the prior setting operations.
print(df)

# A where operation with setting
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)


# Missing Data
# pandas primarily uses the value np.nan to represent missing data.
# It is by default not included in computations

# Reindexing allows you to change/add/delete the index on a specified axis.
# This returns a copy of the data
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)

# To drop any rows that have missing data
print(df1.dropna(how='any'))

# Filling missing data
print(df1.fillna(value=5))

# To get the boolean mask where values are nan
print(pd.isna(df1))

# Operations

# Stats

# Operations in general exclude missing data.
# Performing a descriptive statistic
print(df.mean())

# Same operation on the other axis
print(df.mean(1))

# Operating with objects that have different dimensionality and need alignment.
# In addition, pandas automatically broadcasts along the specified dimension
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(s)

print(df.sub(s, axis='index'))


# Apply

# Applying functions to the data
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))


# Histogramming

s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())


# String Methods

# Series is equipped with a set of string processing methods in the str attribute
# that make it easy to operate on each element of the array, as in the code snippet below.
# Note that pattern-matching in str generally uses regular expressions by default
# (and in some cases always uses them)
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s)
print(s.str.lower())


# Merge

# Concat

# pandas provides various facilities for easily combining together Series,
# DataFrame, and Panel objects with various kinds of set logic for the indexes
# and relational algebra functionality in the case of join / merge-type operations
# Concatenating pandas objects together with concat()
df = pd.DataFrame(np.random.randn(10, 4))
print(df)

# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))


# Join

# SQL style merges
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))

# Another example that can be given is
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))


# Append

# Append rows to a dataframe
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)
s = df.iloc[3]
df.append(s, ignore_index=True)
print(df)


# Grouping

# By “group by” we are referring to a process involving one or more of the following steps:
#   Splitting the data into groups based on some criteria
#   Applying a function to each group independently
#   Combining the results into a data structure
df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})
print(df)

# Grouping and then applying the sum() function to the resulting groups
print(df.groupby('A').sum())

# Grouping by multiple columns forms a hierarchical index, and again we can apply the sum function.
print(df.groupby(['A', 'B']).sum())


# Reshaping

# Stack
tuples = list(zip(*[
    ['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']
]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
print(df2)

# The stack() method “compresses” a level in the DataFrame’s columns
stacked = df2.stack()
print(stacked)

# With a “stacked” DataFrame or Series (having a MultiIndex as the index),
# the inverse operation of stack() is unstack(), which by default unstacks the last level
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))


# Pivot Tables

df = pd.DataFrame({
    'A': ['one', 'one', 'two', 'three'] * 3,
    'B': ['A', 'B', 'C'] * 4,
    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
    'D': np.random.randn(12),
    'E': np.random.randn(12)
})
print(df)

# We can produce pivot tables from this data very easily
print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))


# Time Series

# pandas has simple, powerful, and efficient functionality for performing resampling operations
# during frequency conversion (e.g., converting secondly data into 5-minutely data).
# This is extremely common in, but not limited to, financial applications
rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts.resample('5Min').sum())

# Time zone representation
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)

ts_utc = ts.tz_localize('UTC')
print(ts_utc)

# Converting to another time zone
print(ts_utc.tz_convert('US/Eastern'))

# Converting between time span representations
rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)

ps = ts.to_period()
print(ps)

print(ps.to_timestamp())

# Converting between period and timestamp enables some convenient arithmetic functions to be used.
# In the following example, we convert a quarterly frequency with year ending in November to 9am
# of the end of the month following the quarter end
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
print(ts.head())


# Categoricals

# pandas can include categorical data in a DataFrame
df = pd.DataFrame({
    "id": [1, 2, 3, 4, 5, 6],
    "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']
})

# Convert the raw grades to a categorical data type
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])

# Rename the categories to more meaningful names (assigning to Series.cat.categories is inplace!).
df["grade"].cat.categories = ["very good", "good", "very bad"]

# Reorder the categories and simultaneously add the missing categories
# (methods under Series .cat return a new Series by default).
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df["grade"])

# Sorting is per order in the categories, not lexical order
print(df.sort_values(by="grade"))

# Grouping by a categorical column also shows empty categories.
print(df.groupby("grade").size())


# Plotting
import matplotlib.pyplot as plt

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()

# On a DataFrame, the plot() method is a convenience to plot all of the columns with labels
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
print(plt.figure())
print(df.plot())
print(plt.legend(loc='best'))


# Getting Data In/Out

# CSV

# Writing to a csv file.
df.to_csv('foo.csv')

# Reading from a csv file.
print(pd.read_csv('foo.csv'))

# HDF5
# Reading and writing to HDFStores.
# Writing to a HDF5 Store
df.to_hdf('foo.h5', 'df')
print(pd.read_hdf('foo.h5', 'df'))

# Excel
# Reading and writing to MS Excel.
# Writing to an excel file
df.to_excel('foo.xlsx', sheet_name='Sheet1')
print(pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA']))


# Gotchas
# If you are attempting to perform an operation you might see an exception like
try:
    if pd.Series([False, True, False]):
        print("I was true")
except ValueError as e:
        print(e)





print('\n\n\n\n')



titanic_df = pd.read_csv('titanic.csv', index_col=None, na_values=['NA'])
print(titanic_df.head())
print(titanic_df.describe())
print(titanic_df.drop(['Name', 'Parch', 'PassengerId', 'Ticket'], axis=1).head())
print(titanic_df.isnull().sum())
print(pd.value_counts(titanic_df['Survived']).plot.bar())
print(titanic_df['Survived'].mean())
print(titanic_df.groupby(['Sex']).mean())
print(titanic_df.groupby(['Sex', 'Pclass']).mean())
print(titanic_df[titanic_df['Age'] < 18].groupby(['Sex', 'Pclass']).mean())

print('\n\n\n\n')

import quandl
quandl.ApiConfig.api_key = ''
apple = quandl.get('WIKI/AAPL')
ms = quandl.get('WIKI/MSFT')
print(ms.head())
print(ms['Adj. Close'].plot())
print(ms.index)
print(ms['2018']['Adj. Close'].plot())
print(ms['2018-03']['Adj. Close'].plot())
print(ms['2018-01-01':'2018-03-31']['Adj. Close'].plot())
ms_price = ms[['Adj. Close']]
apple_price = apple[['Adj. Close']]
ms_price.rename(columns={'Adj. Close': 'AAPL'}, inplace=True)
both_stocks = ms_price.join(apple_price, how='inner')
print(both_stocks.plot())
print(both_stocks.loc['2017'].plot())

both_stocks['2017'].rolling(min_periods=10, window=60, center=False).mean().plot()
both_stocks['2017'].rolling(min_periods=10, window=60, center=False).std().plot()








