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
with open('c:/Users/KirkLaptop/Documents/Bootcamp/python_challenge/budget_data.csv', newline="") as csvfile:
    profit_data = csv.reader(csvfile, delimiter=",")
     
#add up total number of months in dataset
    row_index = -1

    for row in profit_data:
        if row:
            row_index +=1
            rows = int(row_index)
                    
#create list for P/L figures and sum the profits and losses column 
#P_Ls = []
    #Total_profit = []
    #Total_profit = {"Profit/Losses" : ()}
    
    profit = 0

    for row in profit_data:
        if row:
            profit=profit+int(row[1])
            profit.append(profit)
#P_Ls = profit_data{"Profit/Losses":[1]}
#sum all profits and losses

    print("Total Months: ",rows)
    print("Total Profit: ",profit)
    print("Average Change: ")
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")

with open("PyBankOutput.txt", "w") as text_file:
    text_file.write("Total Months: ",rows)
    text_file.write("Total Profit: ",profit)
    text_file.write("Average Change: ")
    text_file.write("Greatest Increase in Profits: ")
    text_file.write("Greatest Decrease in Profits: ")
