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

# Using with statement open the file as text file.
# with open(file_to_save,'w') as txt_file:
    # Write three counties to the file.
#    txt_file.write("Counties in the Election\n-------------------------\n")
#    txt_file.write("Arapahoe\nDenver\nJefferson")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here.
    # read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # print the header row
    #next() method used to skip 1st row of the file 
    headers = next(election_data)
    print(headers)
    