import csv
from email import header
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0
# Print the candidate name
candidate_options = []
# Decalre the empty dictionary
candidate_votes = {}

# Winning candidate amd Einning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file. 
    for row in file_reader:
            # 2. Add the total vote count
            total_votes +=1

            candidate_name = row[2]
            # If the candidate does not match any existing candidtae...
            if candidate_name not in candidate_options:
                # Add it to the list of candidates. 
                candidate_options.append(candidate_name)
                # Begin tracking that candidates vote count.
                candidate_votes[candidate_name] = 0 
                # Add a vote to that candidates count
            candidate_votes[candidate_name] += 1
        
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
  
                  
 
# 3. Print the total votes.
print(total_votes)

print(candidate_options)

print(candidate_votes)

print(votes)

print(winning_candidate_summary)
    
    