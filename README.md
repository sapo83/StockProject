# Script to check stock prices daily


I have a stock portfolio that I use a 25% trailing stop strategy. I use the highest stock price since I've owned the stock to calculate the trailing stop. The trailing stop is calculated by subtracting 25% from the highest price. This means that every day I have to check the stock prices & keep track if there is a new high. For entirely too long, I've been doing this myself every day & keeping all the data in an Excel file. This is my attempt to automate the process.

My idea is to have a bash driver script that will eventually run everything in one command. I separated out the functions into their own file. I'm not sure how helpful that will be but right now it seems likes a nice idea. I also have a test file.

2019-5-5 - I added a script to create a mock portfolio. It takes a list of stocks & randomly generates the data needed. I wrote a script that has code in it that I don't need right now but may want in the future. I started a bash driver script that accepts user input. Eventually, this will allow a user to add stocks to the portfolio. 

Files
  - stock.driver.sh - driver script.
  - stock.py - accepts input CSV, applies functions to data
  - stock_functions.py - functions for use in stock.py
  - test.stock.csv - input CSV file with the current data: Company, Symbol, Buy Date, Buy Price, Shares, High, Trailing Stop
  - create.portfolio.py - creates a mock portfolio using stock.list as input
  - stock.list - list of 10 stock symbols
  - mock_portfolio_functions.py - functions to help create mock portfolio
  - stock.UI.driver.sh - driver script that takes user input
  - things.for.later.py - functions I wrote but don't need right now

Future Work
  - Script that allows user to add stocks to the portfolio
  - Script that allows the user to remove stocks from the portfolio
  - Keep all sold/buy data in different file
  - Some kind of error message when stock symbol isn't found
