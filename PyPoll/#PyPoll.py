#PyPoll

import os
import csv

from pathlib import Path

#read in file
data_folder = Path("Bootcamp/python_challenge/")
election_data = data_folder / "election_data.csv"

# create dictionary
election_results = dict()

#read csv file into new dict election_results
with open('c:/Users/KirkLaptop/Documents/Bootcamp/python_challenge/election_data.csv') as csvfile:
    election_results = csv.reader(csvfile)

    votes = []    
#add up total number of months in dataset
    row_index = -1

    for row in election_results:
        if row:
            row_index +=1
            rows = [int(row_index)]
                    
    print(rows)