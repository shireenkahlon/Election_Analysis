import csv
import os
# assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'
# file path to open to
file_to_load = os.path.join("Resources", "election_results.csv") 
# open file using with
# file path to save to
file_to_save = os.path.join("analysis", "election_results.txt")
# open file and save new variable
# with open(file_to_save, "w") as txt_file:

with open(file_to_load) as election_data:


    # analysis of data
    # read file
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    print(header)
    
    # print row in csv vile
    # for row in file_reader:
        # print(row[0])

# close file
# txt_file.close()





# Pseudocode
# The data we need to retrieve
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular votes

#close file

