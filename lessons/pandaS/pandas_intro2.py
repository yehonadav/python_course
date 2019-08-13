import numpy as np
import pandas as pd

# print('loading hard-coded data to a data frame')
# df = pd.DataFrame(
#     [
#         ['Jan', 58, 46, 77, 22, 2.2],
#         ['Feb', 66, 48, 78, 21, 1.2],
#         ['Mar', 98, 41, 97, 31, 1.5],
#         ['Apr', 45, 56, 84, 27, 2.2],
#         ['May', 54, 55, 79, 25, 0.0],
#         ['Jun', 67, 43, 95, 26, 0.12],
#         ['Jul', 73, 52, 107, 29, 0.82],
#         ['Aug', 73, 51, 101, 30, 2.4],
#         ['Sep', 72, 58, 103, 20, 1.7],
#         ['Oct', 83, 42, 96, 32, 1.56],
#         ['Nov', 90, 46, 80, 23, 1.11],
#         ['Dec', 69, 49, 100, 28, 2.97]
#     ],
#     index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
#     columns=['month', 'avg_high', 'avg_low', 'record_high', 'record_low', 'avg_precipitation']
# )

filename = __file__.replace('pandas_intro2.py', 'weather.txt')
df = pd.read_csv(filename)
# https://www.w3resource.com/python-exercises/pandas/index.php
# https://github.com/codebasics/py/blob/master/pandas/21_sql/pandas_sql.ipynb
