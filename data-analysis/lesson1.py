#Working with Pandas
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style


start = datetime.datetime(2014, 1, 1)
end = datetime.datetime(2018, 5, 24)

# Use the The Investors Exchange (IEX) Data API
df = web.DataReader('F', 'iex', start, end)
#Print Pulled Data 
print(df.head())
#Format Data
#Change Index
df.reset_index(inplace=True)
df.set_index("date", inplace=True)
#Drop Column - axis=0 to drop a row, axis=1 to drop a column 
#df = df.drop("volume", axis=1);print(df.head())

style.use('fivethirtyeight')
df['high'].plot()
plt.legend()
plt.show()