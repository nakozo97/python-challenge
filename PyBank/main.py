# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)


# Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv

#Path to collect data
csvpath = os.path.join("budget_data.csv")
        
        #Method 2:Improved Reading using CSV module

#Data lists
profit = []
calendar_date = []
change_monthly = []

month_count = 0
initial_profit = 0
total_profit = 0
total_profit_change = 0

with open(csvpath) as csvfile:

        #CSV reader specifies delimiter and avariable that holds contents
        csvreader = csv.reader(csvfile, delimiter =',')
        #print(csvreader)
        
        #Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
        #print(f"Header: {csv_header}"")

        #Read each row of data after the header
        for row in csvreader:
                
                ## The total number of months included in the dataset
                month_count = month_count + 1
                
                # For readability, it can help to assign your values to variables with descriptive names
                calendar_date.append(row[0])
                
                #Total_profit
                profit.append(row[1])
                total_profit = total_profit + int(row[1])

                #Month to month change. (initial_profit=0)
                # The net total amount of "Profit/Losses" over the entire period
                final_profit = int(row[1])

                change_monthly_profit = (final_profit - initial_profit)

                change_monthly.append(change_monthly_profit)

                total_profit_change = total_profit_change + change_monthly_profit
                initial_profit = final_profit

                #Profit average change
                # The average of the changes in "Profit/Losses" over the entire period
                #average_profit_change = (total_profit_change/month_count)
                average_profit_change = sum(change_monthly)/len(change_monthly)

# The greatest increase in profits (date and amount) over the entire period
                greatest_profit_increase = max(change_monthly)
                greatest_profit_increase_date = calendar_date[change_monthly.index(greatest_profit_increase)]

# The greatest decrease in losses (date and amount) over the entire period
                greatest_profit_decrease = min(change_monthly)
                greatest_profit_decrease_date = calendar_date[change_monthly.index(greatest_profit_decrease)]

# As an example, your analysis should look similar to the one below:
# Financial Analysis
print("Financial Analysis")
# ----------------------------
print("----------------------------")
# Total Months: 86
print(f'Total Months: {month_count}')
# Total: $38382578
print(f'Total: ${total_profit}')
# Average  Change: $-2315.12
print(f'Average Change: ${round(average_profit_change,2)}')
# Greatest Increase in Profits: Feb-2012 ($1926159)
print(f'Greatest Increase in Profits: {greatest_profit_increase_date} (${greatest_profit_increase})')
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
print(f'Greatest Decrease in Profits: {greatest_profit_decrease_date} (${greatest_profit_decrease})')

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#output = PyBank_analysis.txt
with open('PyBank_analysis.txt', 'w') as text:
        # Financial Analysis
        text.write("Financial Analysis")
        text.write("\n")
        # ----------------------------
        text.write("----------------------------")
        text.write("\n")
        # Total Months: 86
        text.write(f'Total Months: {month_count}')
        text.write("\n")
        # Total: $38382578
        text.write(f'Total: ${total_profit}')
        text.write("\n")
        # Average  Change: $-2315.12
        text.write(f'Average Change: ${round(average_profit_change,2)}')
        text.write("\n")
        # Greatest Increase in Profits: Feb-2012 ($1926159)
        text.write(f'Greatest Increase in Profits: {greatest_profit_increase_date} (${greatest_profit_increase})')
        text.write("\n")
        # Greatest Decrease in Profits: Sep-2013 ($-2196167)
        text.write(f'Greatest Decrease in Profits: {greatest_profit_decrease_date} (${greatest_profit_decrease})')
        text.write("\n")
        
