import datetime
import numpy
import pandas
import random
from mock_portfolio_functions import *
from stock_functions import *
from sys import argv

### variables for later use
randDateList = list()
i = 0

### input file should be a list of stock symbols, one per line
script, inFile, outFile = argv

### Set start date
start_date = datetime.date(year=2015, month=1, day=1)
today = datetime.datetime.now().date()

### Read input file into list
stockList = [line.rstrip('\n') for line in open(inFile)]

### create dataframe out of stock list
df = pandas.DataFrame(stockList, columns = ['Symbol'])

### alphabetize dataframe by symbol
df = df.sort_values('Symbol', axis=0)

### generate list of random dates
while i < len(stockList):
    rando = get_random_date(start_date)
    randDateList.append(rando.isoformat())
    i = i + 1

### add list of random dates to data frame as Buy Date
df['Buy Date'] = randDateList

### generate Buy Price columnd
df['Buy Price'] = numpy.random.uniform(5, 200, df.shape[0])
df['Buy Price'] = df['Buy Price'].round(2)
#df['Buy Price'] = df['Buy Price'].astype(float)

### generate number of shares column in data frame
df['Shares'] = numpy.random.randint(1, 30, df.shape[0])

### generate High column
df['High'] = numpy.random.uniform(df['Buy Price'], 200, df.shape[0])
df['High'] = df['High'].round(2)

### generate Trailing Stop column
df['Trailing Stop'] = df['High'].apply(calculate_trailing_stop)

df['Company'] = df['Symbol'].apply(get_company)

cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

df.to_csv(outFile, index = False)
