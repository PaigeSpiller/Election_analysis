# The data we need to retrieve 
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'
#Open the exlection results and read the file
#with open(file_to_load) as election_data:
    # to do: perform analysis
#    print(election_data)
#close the file
#election_data.close()

#import csv
#import os
# Assign a variable for the file to load and the path
#file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read the file
#with open(file_to_load) as election_data:
#    #print the file object
#    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis","election_analysis.txt")
# Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
    # write three counties to the file
#    txt_file.write("Counties in the Election\n--------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter
total_votes = 0
# Canditate Options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    # Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #Print the ccandidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
        
# Save the results to our text file
with open(file_to_save, "w") as txt_file:
#Print the final vote count to the terminal
    election_results = (f"\nElection Results\n" f"-------------------------\n" f"Total Votes: {total_votes:,}\n" f"-------------------------\n")
    #print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts
    # 1. iterate through the candidate list
    for candidate_name in candidate_votes:
    # 2. retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
    # 3. calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
    # print out each candidates name, vote count, and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
    # save the candidate results to our text file
        txt_file.write(candidate_results)
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate;s name
            winning_candidate = candidate_name
# print out each candidates name, vote count, and percentage of votes
    winning_candidate_summary = (f"-------------------\n" f"Winner: {winning_candidate}\n" f"Winning Vote Count: {winning_count:,}\n" f"Winning Percentage: {winning_percentage:.1f}%\n" f"-------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    #election_results = (f"\nElection Results\n" f"-------------------------\n" f"Total Votes: {total_votes:,}\n" f"-------------------------\n")
#print(election_results, end="")