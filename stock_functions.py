import lxml
from lxml import html
import requests


### removes $ & , from dollar amounts, returns float
def dollars_to_float(dollar_str):
    return float(dollar_str.replace("$","").replace(",",""))


### get current stock price based on symbol
def get_current_price(sym):
    try:
        url = "https://www.nasdaq.com/symbol/" + sym
        page = requests.get(url)
        tree = html.fromstring(page.content)
        div = tree.xpath('//*[@id="qwidget_lastsale"]/text()')[0].strip("$")
        return(div)
    except IndexError:
        return("NF")


### check if current price is higher than the high recorded in df
def check_high(vals):
    high = vals[5]
    current_price = float(vals[7])
    if current_price > high:
        return(current_price)
    else:
        return(high)


### calculate trailing stop
def calculate_trailing_stop(val):
    return(round(val - (val*0.25), 2))
