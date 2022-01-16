import csv
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
           # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")

    print(election_results, end="")
# After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)

        txt_file.write(candidate_results)

       # print(f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
           
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
  

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
    
    