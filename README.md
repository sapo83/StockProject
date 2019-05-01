# Script to check stock prices daily


I have a stock portfolio that I used a 25% trailing stop strategy with. I use the highest stock price since I've owned the stock to calculate the trailing stop. The trailing stop is calculated by subtracting 25% from the highest price. This means that every day I have to check the stock prices & keep track if there is a new high. For entirely too long, I've been doing this myself everyday & keeping all the data in an Excel file. This is my attempt to automate the process.

My idea is to have a bash driver script that will eventually run everything in one command. I separated out the functions into their own file. I'm not sure how helpful that will be but right now it seems likes a nice idea. I also have a test file.

Files
  - stock.driver.sh - This is the driver script.
  - stock.py - accepts input CSV, applies functions to data
  - stock_functions - functions for use in stock.py
  - test.stock.csv - input CSV file with the current data: Company, Symbol, Buy Date, Buy Price, Shares, High, Trailing Stop

Future Work
  - Script that allows user to add stocks to the portfolio
  - Script that allows the user to remove stocks from the portfolio
  - Keep all sold/buy data in different file
  - Some kind of error message when stock symbol isn't found
