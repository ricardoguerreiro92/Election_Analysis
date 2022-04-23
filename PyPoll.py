#The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number fo votes each candidate won.
# 5. The winner of the election based on popular vote.


# Add dependencies
# Import csv module
import csv
# Import os module
import os
# Assign a variable for the file to load a file from a path
file_to_load = os.path.join('resources','election_results.csv')

# Assign a variable to save the file to a path
file_to_save = os.path.join('analysis','election_analysis.txt')

# 1. Initializze a total vote counter.
total_votes = 0

# List of candidates
candidate_options = []

# Declaring empty dictionary for candidate votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    #next() method used to skip 1st row of the file 
    headers = next(election_data)
    
    # Print each row in the csv file.
    for row in file_reader:

        # 2. Add to the total of vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]
       
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add candidate name to the candidate list
            candidate_options.append(candidate_name)
            #2. Begin tracking that candidate vote count
            candidate_votes[candidate_name] = 0
        #increments number of votes per candidate
        candidate_votes[candidate_name] += 1
             
with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results,end = "")
    
    # Save the final vote count to the text file
    txt_file.write(election_results)       
           
    # Determine the percentage of votes for each candidate by looping through the counts.

    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        
        # 3. Calculate the percentage of votes
        votes_percentage = float(votes) / float(total_votes) * 100
        
        # Declares the percentage of votes per candidate in a variable to be printed later on
        candidate_results = (
            f"{candidate_name}: received {votes_percentage:.1f}% of the votes.\n"
            )
            
        # Print each candidate, their voter count, and percentage to the terminal.        
        print(candidate_results)
        
        # Save the candidate results to our text file
        txt_file.write(candidate_results)
               
        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (votes_percentage > winning_percentage):
            # 2. if true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = votes_percentage
            # 3. and sets winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # Print the winning candidate result to the terminal
    winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n"        
        )
        
    print(winning_candidate_summary)
        
    # Save the winning candidate result to the txt file
    txt_file.write(winning_candidate_summary)