#!/bin/bash

### Driver for stock script

python3 create.portfolio.py stock.list mock.portfolio.csv

python3 stock.py mock.portfolio.csv test.out.csv
