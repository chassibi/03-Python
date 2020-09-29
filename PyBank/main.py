import os
import csv

# create a variable 'csvpath'

csvpath = os.path.join("Resources", "budget_data.csv")

# set variables
total_months = []
total_profits_losses = []
average_profits_losses = []
greatest_increase_profits = []
greatest_decrease_losses = []


# to read the csv file

with open(csvpath) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)

# file too big so you can't see it; listed as object

# to use loop function, use head function so that for loop knows where to start

    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

    for x in csvreader:
        total_months.append(x[0])
        print(len(total_months))

        total_profits_losses.append(int(x[1]))
        print(sum(total_profits_losses))
    

