# Pandas Exercises  
  
  
(1)  
* import numpy as np  
* import pandas as pd  
* create a __name__ == "__main__" condition  
* in define this variable:  
```python
data={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
```    
* create a dataframe and print it  
* view dataframe head  
* view dataframe tail  
* view dataframe head of 3  
* view dataframe tail of 3  
* view dataframe shape  
* view dataframe info  
* view dataframe description  
* view data types  

(2)  
* create a dataframe  
* select a column  
* select 2 columns  
* select the first row  
* select the first element of first column  
  
(3)  
* create a dataframe  
* rename its columns  
* check for empty values  
* check for not-empty values  
* drop all rows that contain null values  
* drop all columns that contain null values  
* drop all rows that have less than 3 non null values
* replace all null values with 99  
* rename all columns to lowercase  
* rename 1 column  
* set Y as  
* increase all indexes by 1  
  
(4)  
* create a dataframe  
* get the rows where the minimal value of X is bigger than 84  
* get the rows where the minimal value of Y is bigger than 86 and smaller than 94  
* sort values of Y in ascending order  
* sort values of Y in descending order  
* sort values of Y in ascending order then Z in descending order  
* group values from one column  
* group values from 2 columns  
* get the mean values in Z, grouped by the values in X  
* create a pivot table that groups by X and calculates the mean of Y and Z  
* get the average across all columns for every unique X group  
* apply the function np.mean() across each column  
* apply the function np.max() across each row 
  
(5)  
* create 2 dataframes: df1, df2
* Add the rows in df1 to the end of df2 (columns should be identical)  
* Add the columns in df1 to the end of df2 (rows should be identical)  
* make SQL-style join the columns in df1 with the columns on df2 where the rows for col have identical values. The 'how' can be 'left', 'right', 'outer' or 'inner'  

  
(6)  
* create a dataframe  
* Summarize statistics for numerical columns  
* get the mean of all columns  
* get the correlation between columns in a DataFrame  
* get the number of non-null values in each DataFrame column  
* get the highest value in each column  
* get the lowest value in each column  
* get the median of each column  
* get the standard deviation of each column  
  
(7)    
* create a dataframe from CSV file  
* create a dataframe from a delimited text file (like TSV)  
* create a dataframe from an Excel file  
* create a dataframe from a SQL table/database  
* create a dataframe from a JSON formatted string, URL or file.  
* parse an html URL, string or file and extracts tables to a list of dataframes  
* take the contents of your clipboard and pass them to read_table()  
* create a dataframe from a dict, keys for columns names, values for data as lists  
  
(8)  
* Write to a CSV file  
* Write to an Excel file  
* Write to a SQL table  
* Write to a file in JSON format    
  
  
more exercises:  
---------   
  
if you have ideas for any kind of exercises please open up an issue with:  
* the exercise title  
* exercise description  
* recommended dependencies & tools  
* steps pointing to the solution  
* a working solution  
  