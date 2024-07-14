import os
import csv

#Get path to file
path_to_file = os.path.join("/Users/Sweet/OneDrive/Desktop/budget_data.csv")

# Establish variables
total_months = 0
net_total = 0
previous_profit_loss = None
changes = []
dates = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = float('inf')  # Set to infinity for comparison
greatest_decrease_date = ""

# Open the CSV file
with open(path_to_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Count m
    # Process each row
    for row in csv_reader:
        total_months += 1  # Count months
        date = row[0]  # Get the date
        profit_loss = int(row[1])  # Convert to integer
        net_total += profit_loss  # Sum profit/losses
        dates.append(date)  # Store the date

        # Calculate change from the previous month
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            # Check for greatest increase
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            
            # Check for greatest decrease
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date

        previous_profit_loss = profit_loss  # Update previous month value

# Calculate average change
average_change = sum(changes) / len(changes) if changes else 0

# Print results
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in profits: {greatest_increase_date} (${greatest_increase})")
print(f"The Greatest Decrease in profits: {greatest_decrease_date} (${greatest_decrease})")











