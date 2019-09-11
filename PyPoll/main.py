import csv

# Opens the file into a dictionary reader object
with open('election_data.csv') as election_data:
    election_dict = csv.DictReader(election_data)

    total_votes = 0
    
    # Creates a dictionary that will contain "Candidate Name: x, ..." where x is # of votes
    vote_count = {}
    
    # Iterates through every voter.....
    for row in election_dict:

        total_votes += 1

        # If the voter's choice isn't in vote_count dictionary, then add that candidate with 1 vote
        if vote_count.get(row["Candidate"]) is None:
            vote_count[row["Candidate"]] = 1
        
        # Otherwise, add one to the tally for the voter's chosen candidate
        else: 
            vote_count[row["Candidate"]] +=1


    # We've gone through all the voters- tally and print results--
    
    print("Election Results")
    print("------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------")
        
    # Set variables that will be used to name the winner
    winner_votes = 0
    winner_name = "nobody"
    
    # Go through all of the candidates in the vote_count dictionary
    for key in vote_count:
       
       # Check to see if this candidate has the most votes
        if vote_count[key] > winner_votes:
            winner_votes = vote_count[key]
            winner_name = key
        
        # Prints this candidate's results
        print ("{0} : {1:.3%} ({2})".format(key,(vote_count[key]/total_votes),vote_count[key]))

    # We are done checking and printing out results-- print out the winner
    print("------------------")
    print(f"Winner: {winner_name}")
    print("------------------")


      # Write results to text file
    resultsfile = open("pyPollResults.txt","w") 

    print("Election Results", file = resultsfile)
    print("------------------", file = resultsfile)
    print(f"Total Votes: {total_votes}", file = resultsfile)
    print("------------------", file = resultsfile)

    for key in vote_count:
        print ("{0} : {1:.3%} ({2})".format(key,(vote_count[key]/total_votes),vote_count[key]), file = resultsfile)
 
    print("------------------", file = resultsfile)
    print(f"Winner: {winner_name}", file = resultsfile)
    print("------------------", file = resultsfile)

    resultsfile.close()