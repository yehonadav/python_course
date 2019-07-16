import numpy as np
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

data = {
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

data2 = {
    'A': [44, 54, 56, 9, 77],
    'B': [55, 94, 56, 75, 74],
    'C': [66, 700, 90, 44, 23]
}

data_with_null = dict(data)
data_with_null['X'][0] = None
data_with_null['X'][1] = None
data_with_null['X'][2] = None
data_with_null['Y'][0] = None
data_with_null['Y'][1] = None
data_with_null['Y'][2] = None
data_with_null['Z'][0] = None
data_with_null['Z'][1] = None
data_with_null['Z'][2] = None


def exercise123():
    df = pd.DataFrame(data)
    print(df)
    print(df.head())
    print(df.head(3))
    print(df.tail())
    print(df.tail(3))
    print(df.shape)
    print(df.info())
    print(df.describe())
    print(df.dtypes)


def exercise124():
    df = pd.DataFrame(data)
    print(df[['X']])
    print(df[['X', 'Y']])
    # print(df.iloc[:,0:2])
    # print(df.iloc[:,0:1])
    print(df.iloc[0, :])
    print(df.iloc[0, 0])


def exercise125():
    df = pd.DataFrame(data_with_null)
    df.columns = ['a', 'b', 'c']
    print(df.columns)
    print(df.isnull())
    print(df.notnull())
    print(df.dropna())
    print(df.dropna(axis=1))
    print(df.dropna(axis=1, thresh=3))
    df = pd.DataFrame(data_with_null)
    print(df.fillna(99))
    print(df.rename(columns=lambda x: x.lower()))
    print(df.rename(columns={'X': 'new name'}))
    print(df.set_index('Y'))
    print(df.rename(index=lambda x: x + 1))


def exercise126():
    df = pd.DataFrame(data)
    print(df[df['X'] > 84])
    print(df[(df['Y'] > 86) & (df['Y'] < 94)])
    print(df.sort_values('Y'))
    print(df.sort_values('Y', ascending=False))
    print(df.sort_values(['Y', 'Z'], ascending=[True, False]))
    # we need to iterate if we want to see the group
    print(df.groupby('X'))
    print(df.groupby(['X', 'Y']))
    print(df.groupby('X')['Z'])
    print(df.pivot_table(index='X', values=['Y', 'Z'], aggfunc=np.mean))
    print(df.groupby('X').agg(np.mean))
    print(df.apply(np.mean))
    print(df.apply(np.max, axis=1))


def exercise127():
    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(data2)
    df1.append(df2, sort=False)
    pd.concat([df1, df2], axis=1)
    df1.join(df2, on='X', how='inner')


def exercise128():
    df = pd.DataFrame(data)
    df.describe()
    df.mean()
    df.corr()
    df.count()
    df.max()
    df.min()
    df.median()
    df.std()


def exercise129():
    pd.read_csv('titanic.csv')
    pd.read_csv('weather.txt')
    pd.read_excel('foo.xlsx')
    # db = create_engine('sqlite:///pandasdb.db')
    # pd.read_sql(
    #     ('select "Timestamp","Value" from "MyTable" '
    #      'where "Timestamp" BETWEEN %(dstart)s AND %(dfinish)s'),
    #     db, params={
    #         "dstart": datetime(2014, 6, 24, 16, 0),
    #         "dfinish": datetime(2014, 6, 24, 17, 0)
    #     }, index_col=['Timestamp'])
    pd.read_json('https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/data.json', orient='columns')
    # make sure lxml, html5lib, bs4, is installed
    pd.read_html("https://pandasbootcamp.herokuapp.com/")
    pd.read_clipboard()
    pd.DataFrame(data)


def exercise130():
    df = pd.DataFrame(data)
    df.to_csv('exercise130.csv')
    df.to_excel('exercise130.xlsx')

    db = create_engine('sqlite:///pandasdb.db')
    df.to_sql('data', db)

    df.to_json('exercise130.json')


if __name__ == "__main__":
    # https://pandas.pydata.org/
    exercise123()
    exercise124()
    exercise125()
    exercise126()
    exercise127()
    exercise128()
    exercise129()
    exercise130()
