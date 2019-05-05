import numpy
import pandas
import sys
from stock_functions import *
from sys import argv

script, inFile, outFile = argv

sellList = list()

df = pandas.read_csv(inFile)

### strip $ & , from all monetary values, return float
#df['Buy Price'] = df['Buy Price'].apply(dollars_to_float)
#df['High'] = df['High'].apply(dollars_to_float)
#df['Trailing Stop'] = df['Trailing Stop'].apply(dollars_to_float)

### get current price of stock
df['Current Price'] = df['Symbol'].apply(get_current_price)

### drop any rows with no current price found
df = df[df['Current Price'] != "NF"]

### check if current price is higher than original high
df['High'] = df.apply(check_high, axis = 1)

### calculate trailing stop
### eventually I want to rewrite this to only calculate the trailing stop if there is a new high
df['Trailing Stop'] = df['High'].apply(calculate_trailing_stop)

### check if sotck should be sold; if trailing stop is >= current price, sell; else hold
df['Sell'] = df.apply(sell_check, axis = 1)

### convert Sell solumn to list
sellList = df['Sell'].tolist()
### remove all HOLD values from sell list
while "HOLD" in sellList: sellList.remove("HOLD")

### print data frame
print(df)

df = df[~df['Symbol'].isin(sellList)]
print(df)

df = df.drop(columns = ['Sell'])

print(df)

### write data frame to csv
df.to_csv(outFile, index = False)
