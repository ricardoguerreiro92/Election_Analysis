# Election Analysis

### <strong>Overview of Election Audit:</strong>
- The purpose of this analysis is to determine the number of votes for each county and candidate.<br>We will also determine the largest turnout county and declare the winner by popular vote in percentages.</br>

### Election Audit Results
![Votes](/resources/election_results.png)

### Total Votes
- There is a total of 369,711 votes.

### Votes by County
- 38,855 votes in Jefferson county making 10.5% of the total votes.
- 306,055 votes in Denver county making 82.8% of the total votes.
- 24,801 votes in Arapahoe county making 6.7% of the total votes.

### Turnout County
- <strong>Denver is the largest county turnout with 306,055 votes, an 82.8% of the total votes.</strong>
  
### Votes by Candidate
- There was a total of 85,213 votes for Charles Casper Stockham making 23% of the total votes.
- There was a total of 272,892 votes for Diana DeGette making 73.8% of the total votes.
- There was a total of 11,606 votes for Raymon Anthone Doane making 3.1% of the total votes.

### Election Winner

- <strong>*Diana DeGette has won*</strong> the election acquiring a <strong>*total of 272,892 votes*</strong>, winning with a clear <strong>*73.8% of the total votes*</strong>.

### Election-Audit Summary
```py
    import csv
    import os

    file_to_load = os.path.join("Resources", "election_results.csv")
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    total_votes = 0
    candidate_options = []
    candidate_votes = {}
    county_list = []
    county_votes = {}
    winning_candidate = ""
    winning_count = 0
    winning_percentage = 0
    county_turnout = ""
    county_count = 0

    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
        header = next(reader)

        for row in reader:
            total_votes += 1
            candidate_name = row[2]
            county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] += 1
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

    with open(file_to_save, "w") as txt_file:
            election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n")
        print(election_results, end="")

        txt_file.write(election_results)

        for county_name in county_list:
            votes = county_votes[county_name]
            vote_percentage = float(votes) / float(total_votes) * 100
            county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(county_results)
            txt_file.write(county_results)

            if (votes > county_count) and (vote_percentage > winning_percentage):
                county_count = votes
                county_turnout = county_name

        turnout = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout: {county_turnout}\n"
            f"-------------------------\n"
        )
        print(turnout)
        txt_file.write(turnout)

        for candidate_name in candidate_votes:
            votes = candidate_votes.get(candidate_name)
            vote_percentage = float(votes) / float(total_votes) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
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
```
- This code can also be used for Presidential elections with simple modifications, since we already have county & candidates all we need to do is add votes by states and create a dictionaries to organize the counties by states and get the results by county & state. We can go as far as add townships and cities by nesting dictionaries together to organize and hold values.
    
- One other way we could modify this code for is to know if a bill is passed by the Congress. Instead of having candidates & counties we would have if a bill is voted to pass by the Senate and the House of Representative considering the number of votes for said bill, if passed so then it would declare the bill to be sent to the President of the United States.

    - Source code python 3.10.4
