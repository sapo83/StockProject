import datetime
from faker import Faker
import lxml
from lxml import html
import re
import requests


fake = Faker()
r1 = re.compile("(.*?)\s*\(")

def get_random_date(start_date):
    today = datetime.datetime.now().date()
    return(fake.date_between(start_date=start_date, end_date=today))

def parse_buy_date(date):
    year = int(date.split("-")[0])
    month = int(date.split("-")[1])
    day = int(date.split("-")[2])
    new_start = datetime.date(year = year, month = month, day = day)
    return(get_random_date(new_start))

def get_company(sym):
    try:
        url = "https://www.nasdaq.com/symbol/" + sym
        page = requests.get(url)
        tree = html.fromstring(page.content)
        div = tree.xpath('//*[@id="qwidget_pageheader"]/h1/text()')[0]
        m1 = r1.match(div)
        return(m1.group(1).lstrip().replace(' Common Stock', ''))
    except IndexError:
        return("NF")
