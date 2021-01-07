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

# set accumulator
total_votes = 0

#create a list for candidates
candidate_options = []

#create a dictionary for candidates votes
candidate_votes = {}

#variable for winning candidate
winning_candidate = ""
# variable for winning count of votes
winning_count = 0
#variable for winning percentage of votes

winning_percentage = 0
# with open(file_to_save, "w") as txt_file:

with open(file_to_load) as election_data:


    # analysis of data
    # read file
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    print(header)

    # count through rows - accumulator - add up each row
    for row in file_reader:
        total_votes += 1
        # get names of candidates
        candidate_name = row[2]
        #if candidate name doesn't match existing candidate
        if candidate_name not in candidate_options:
        #add candidate name to list
            candidate_options.append(candidate_name)
            #track candidate's vote count
            candidate_votes[candidate_name] = 0
        #track candidates votes
        candidate_votes[candidate_name] +=1
        #iterate through candidate votes
    for candidate_name in candidate_votes:
        #retrieve votes
        votes = candidate_votes[candidate_name]
        percentage_votes = float(votes)/float(total_votes) * 100
        print(f'{candidate_name} received {percentage_votes:.1f}% of the total votes')
    # To do: print out each candidate's name, vote count, and percentage of
        print(f'{candidate_name}: {percentage_votes:.1f}%, {votes}\n')
    #Are votes bigger than winning votes?
        if (votes > winning_count) and (percentage_votes > winning_percentage):
            winning_count = votes
            winning_percentage = percentage_votes
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"----------------------\n"
        f"The winning candidate is {winning_candidate}\n"
        f"The winning candidate received {winning_percentage:.1f}% of the total votes\n"
        f"The winning candidate received {winning_count} total votes\n"
        f"Congratulations to the winner of the congressional race!\n"
        f'-------------------\n'
    )
    print(winning_candidate_summary)
        


    # print candidate options
    print(candidate_options)
    #print candidate_votes
    print(candidate_votes)
        
    
    # print row in csv vile
    print(total_votes)
    
    

  


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

