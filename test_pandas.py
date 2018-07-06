import datetime as dt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12, 31)

df = web.DataReader('TSLA', start, end)
print(df.head())
