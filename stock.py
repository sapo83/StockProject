import numpy
import pandas
import sys
from stock_functions import *

inFile = sys.argv[1]

df = pandas.read_csv(inFile)

### strip $ & , from all monetary values, return float
df['Buy Price'] = df['Buy Price'].apply(dollars_to_float)
df['High'] = df['High'].apply(dollars_to_float)
df['Trailing Stop'] = df['Trailing Stop'].apply(dollars_to_float)

### get current price of stock
df['Current price'] = df['Symbol'].apply(get_current_price)

### drop any rows with no current price found
df = df[df['Current price'] != "NF"]

### check if current price is higher than original high
df['High'] = df.apply(check_high, axis=1)

### calculate trailing stop
### eventually I want to rewrite this to only calculate the trailing stop if there is a new high
df['Trailing Stop'] = df['High'].apply(calculate_trailing_stop)

### print datafram
print(df)

for col in df.columns: 
    print(col)
