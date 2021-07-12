# Election_Analysis
This project will use Python to perform an analysis on  Colorado congressional elections.

## Purpose
The purpose of this project is to analyze an election audit for Colorado’s congressional races that would also work for local and U.S. Senate (in Colorado) races. An audit is conducted to ensure the votes in an election cycle were counted correctly. The audit is one of the most significant aspects of an election to ensure the validity of the election. The analysis of this audit will walk through the steps we created to automate a process that ensures the election went smoothly, no ballots were counted twice, or that no ballot was left uncounted.

## Election-Audit Results
### How many votes were cast in this congressional election?
* Using total_votes as a variable to contain the total number of votes, I set the variable to 0 before automating the process. I used the following code to find that 369,711 total votes were cast in the congressional election:
![Total_Votes_Screenshot](https://github.com/shireenkahlon/Election_Analysis/blob/main/Screenshots/total%20votes%20python%20screenshot.png)

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
* 38,855 votes were casted in Jefferson County (10.51% of the total votes), 306,055 votes were casted in Denver County (82.78% of the total votes), and 24,801 votes were casted in Arapahoe County (6.71% of the total votes). I found these calculations by first creating a list of counties. The code would loop through the rows and display counties which had not been repeated. It would then add a vote for each county name. For the second block of code, I divided each county's numbers by total_votes variable and multiplied this number by 100 to find the percentage. I used the following code block for this analysis:
![votes_per_county](https://github.com/shireenkahlon/Election_Analysis/blob/main/Screenshots/votes%20per%20county%20screenshot.png)

along with this block of code:
![percentage_of_votes](https://github.com/shireenkahlon/Election_Analysis/blob/main/Screenshots/percentage_of_votes.png)

### Which county had the largest number of votes?
Denver county had the highest voter turnout with 306,055 votes. I calculated this by creating a variable for the county with the highest voter turnout and another variable to contain how many voters voted in this particular county. Afterwards, I used a conditional statement to compare each county. If the county the conditional was looking at had the highest voter turnout, it would add that as the largest_county variable until it went to the next county. After completing through all three counties, the largest county would be displayed when executing the python code. I used the following code block:
![largest_county](https://github.com/shireenkahlon/Election_Analysis/blob/main/Screenshots/largest_county.png)

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Charles Casper Stockham received 85,213 or 23.0% of the total votes, Diana DeGette received 272,892 or 73.8% of the total votes, and Raymon Anthony Doane 11,606 received 3.1% of the total votes. I used a list (candidate_options) to hold the three candidates names and a dictionary (cadidate_votes) to hold the candidate name as the key and the number of votes the candidate received as a value. From this, I created a conditional statement to tally each vote per candidate by adding in the name of the candidate to a list and counting their votes; a for loop was used to find the percentage for each candidate. The code is as follows:
![candidate_votes](https://github.com/shireenkahlon/Election_Analysis/blob/main/Screenshots/candidate_votes.png)
Along with the following code:
![Candidate_Percentage](https://github.com/shireenkahlon/Election_Analysis/blob/main/Screenshots/candidate_percentage.png)

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
Diana DeGette won the election with 272,892 votes or 73.8% of the total votes. Variables for the winning candidate, percentage, and count were created and an if then statement finding the highest vote count and highest percentage was implemented. The code is as follows:
![winning_candidate_screenshot](https://github.com/shireenkahlon/Election_Analysis/blob/main/Screenshots/winning_candidate_screenshot.png)

## Election-Audit Summary
This code can be used in various scenarios to help audit local, state legislature, U.S. House, and U.S. Senate races. The code worked within seconds to bring back results for this specific congressional race and thus, can be used for quick results for other races as well. To use this programming code for other races, a few changes could be made. A line of code to connect the candidates to counties should be added (for example, hypothetically, Charles Casper Stockham received 85 votes in Jefferson county). Another way of improving the code for general use is by using with open() instead of os.path.join(). This way, it doesn’t matter what folder the analyst is currently in, but can open a file from the direct name of the file. Finally, one possible solution to confirm the vote is by creating variables and writing code to find out the vote based on party line. Most congressional and state legislature races are based on party line. By counting by party, this would be an extra confirmation of who won the race.







