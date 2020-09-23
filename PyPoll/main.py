# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.


# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

import os
import csv

#Path to collect data
csvpath = os.path.join("election_data.csv")

        #Method 2:Improved Reading using CSV module

#Data lists
Voter_ID = []
County = []
Candidate =[]

with open(csvpath) as csvfile:

        #CSV reader specifies delimiter and avariable that holds contents
        csvreader = csv.reader(csvfile, delimiter =',')
        #print(csvreader)
        
        #Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
        #print(f"Header: {csv_header}"")

        #Read each row of data after the header
        for row in csvreader:
            Voter_ID.append(row[0])
            County.append(row[1])
            Candidate.append(row[2])

Vote_count = int(len(Candidate))

# The total number of votes cast
total_votes = len(Voter_ID)

# A complete list of candidates who received votes
#Unique candidate votes. Used filtering system. 
candidate_Khan_votes = (Candidate.count("Khan"))
candidate_Correy_votes = (Candidate.count("Correy"))
candidate_Li_votes = (Candidate.count("Li"))
candidate_OTooley_votes = (Candidate.count("O'Tooley"))

# The percentage of votes each candidate won
candidate_Khan_percentage = (candidate_Khan_votes/total_votes)*100
candidate_Correy_percentage = (candidate_Correy_votes/total_votes)*100
candidate_Li_percentage = (candidate_Li_votes/total_votes)*100
candidate_OTooley_percentage = (candidate_OTooley_votes/total_votes)*100

# The total number of votes each candidate won


# The winner of the election based on popular vote.
#Winner = mode(candidate_Khan_votes+candidate_Correy_votes+candidate_Li_votes+candidate_OTooley_votes)

#Template: print(f'Average Change: ${round(average_profit_change,2)}')

# As an example, your analysis should look similar to the one below:
# Election Results
print("Election Results")
# -------------------------
print("-------------------------")
# Total Votes: 3521001
print(f'Total Votes: {total_votes}')
# -------------------------
print("-------------------------")
# Khan: 63.000% (2218231)
print(f'Khan: {round(candidate_Khan_percentage,1)}% ({candidate_Khan_votes})')
# Correy: 20.000% (704200)
print(f'Correy: {round(candidate_Correy_percentage,1)}% ({candidate_Correy_votes})')
# Li: 14.000% (492940)
print(f'Li: {round(candidate_Li_percentage,1)}% ({candidate_Li_votes})')
# O'Tooley: 3.000% (105630)
print(f'OTooley: {round(candidate_OTooley_percentage,1)}% ({candidate_OTooley_votes})')
#print("O'Tooley: " + str(int(candidate_OTooley_percentage))% + str(int(candidate_OTooley_votes)))
# -------------------------
print("-------------------------")
# Winner: Khan
print("Winner: Khan")
# -------------------------
print("-------------------------")

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#output = PyPoll_analysis.txt

with open('PyPoll_analysis.txt', 'w') as text:
    # Election Results
    text.write("Election Results")
    text.write("\n")
    # -------------------------
    text.write("-------------------------")
    text.write("\n")
    # Total Votes: 3521001
    text.write(f'Total Votes: {total_votes}')
    text.write("\n")
    # -------------------------
    text.write("-------------------------")
    text.write("\n")
    # Khan: 63.000% (2218231)
    text.write(f'Khan: {round(candidate_Khan_percentage,3)}% ({candidate_Khan_votes})')
    text.write("\n")
    # Correy: 20.000% (704200)
    text.write(f'Correy: {round(candidate_Correy_percentage,3)}% ({candidate_Correy_votes})')
    text.write("\n")
    # Li: 14.000% (492940)
    text.write(f'Li: {round(candidate_Li_percentage,3)}% ({candidate_Li_votes})')
    text.write("\n")
    # O'Tooley: 3.000% (105630)
    text.write(f'OTooley: {round(candidate_OTooley_percentage,3)}% ({candidate_OTooley_votes})')
    text.write("\n")
    # -------------------------
    text.write("-------------------------")
    text.write("\n")
    # Winner: Khan
    text.write("Winner: Khan")
    text.write("\n")
    # -------------------------
    text.write("-------------------------")
    text.write("\n")