#Working with Pandas
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

# Use the The Investors Exchange (IEX) Data API
def get_data(reader,ticker,start,end,retrycount):
    try:
        #df = reader.DataReader('%s' % (ticker), 'morningstar', start, end, retry_count=0)
        df = reader.DataReader('%s' % (ticker), 'iex', start, end, retry_count=0)
        print(df.tail(5))
    except ValueError:
        print('Ticker Symbol %s is not available!' % (ticker))

def plot_data(df,field):
    style.use('fivethirtyeight')
    df['%s' % (field)].plot()
    plt.legend()
    plt.show()

def test_data(start,end):
    df = web.DataReader('F', 'iex', start, end)
    print(df.head())
    return df