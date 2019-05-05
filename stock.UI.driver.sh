#!/bin/bash

#read -p "Would you like to create a mock portfolio? " response1

echo "Would you like to create a mock portfolio?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) python3 create.portfolio.py stock.list mock.portfolio.csv; break;;
        No ) exit;;
    esac
done
