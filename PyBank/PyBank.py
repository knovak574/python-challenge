# PyBank

import os
import csv

from pathlib import Path

#read in file
data_folder = Path("Bootcamp/python_challenge/")
budget_data = data_folder / "budget_data.csv"

# create dictionary
profit_data = dict()

#read csv file into new dict profit_data
with open('c:/Users/KirkLaptop/Documents/Bootcamp/python_challenge/budget_data.csv') as csvfile:
    profit_data = csv.reader(csvfile)

    data = []    
#add up total number of months in dataset
    for row in profit_data:
        data.append(row)
        

print(data)

#Total_months = len(profit_data)



#create list for P/L figures and sum the profits and losses column 
P_Ls = []

#for i in range (len profit_data)
    #sum("Profit/Losses", [1])

#P_Ls = profit_data{"Profit/Losses":[1]}
#sum all profits and losses
#Total_profit = sum(P_Ls)

