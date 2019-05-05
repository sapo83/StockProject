### generate Sell Date column in data frame
df['Sell Date'] = df['Buy Date'].apply(parse_buy_date)
df['Sell Price'] = numpy.random.uniform(df['Buy Price'], 200, df.shape[0])
df['Sell Price'] = df['Sell Price'].round(2)
