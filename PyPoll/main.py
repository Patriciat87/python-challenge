import os
import csv

#Get Path to file
path_to_file = os.path.join("/Users/Sweet/OneDrive/Desktop/election_data.csv")

#Establish variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0
candidate_results = {}

#Open CSV file
with open(path_to_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header (correct file?)
    csv_header = next(csv_reader)
    
    #Create Forloop 
    for row in csv_reader:
        total_votes += 1  # Count total votes
        candidate = row[2]  # Get candidate name
        
        # Count votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1


#Create another forloop

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidate_results[candidate] = {
        "total_votes": votes,
        "percentage": percentage
    }
    
    #Determine who the winner is 
    if votes > max_votes:
        max_votes = votes
        winner = candidate

#Print Results
print("Election Results:")
print(f"Total Votes: {total_votes}")
for candidate, results in candidate_results.items():
    print(f"{candidate}: {results['percentage']:.2f}% ({results['total_votes']})")
print(f"Winner: {winner}")

#Output to txt file
output_path = os.path.join("/Users/Sweet/OneDrive/Desktop/election_results.txt")
with open(output_path, "w") as txt_file:
    txt_file.write("Election Results:\n")
    txt_file.write(f"----------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"----------------------------\n") 
    for candidate, results in candidate_results.items():
                txt_file.write(f"{candidate}: {results['percentage']:.2f}% ({results['total_votes']})\n")
    txt_file.write(f"----------------------------\n")             
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write(f"----------------------------\n") 
