import os
import csv

#Get path to file
path_to_file = os.path.join("/Users/Sweet/OneDrive/Desktop/budget_data.csv")

# Establish all variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = float('inf') 
greatest_decrease_date = ""



#Open the CSV file
with open(path_to_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #Header(first 5 rows of data)
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")


    #Create a forloop to go through each row
    for x in csv_reader:
        total_months += 1 
        date = x[0]  
        profit_loss = int(x[1]) 
        net_total += profit_loss  
        dates.append(date)  

        #Calculations of change from the previous month

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            #greatest increase
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            
            #greatest decrease
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date

        previous_profit_loss = profit_loss  

#Calculate average change
average_change = sum(changes) / len(changes) if changes else 0


#Print results
print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in profits: {greatest_increase_date} (${greatest_increase})")
print(f"The Greatest Decrease in profits: {greatest_decrease_date} (${greatest_decrease})")

Financial_Analysis= print("Financial Analysis")
print(f"Total Months: {total_months}")
print(f"Total: {net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in profits: {greatest_increase_date} (${greatest_increase})")
print(f"The Greatest Decrease in profits: {greatest_decrease_date} (${greatest_decrease})")


output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

#Print results to an output
print(output)

#Write results to text file
output_file = "financial_analysis.txt"
with open(output_file, 'w') as file:
    file.write(output)

print(f"Financial analysis results written to {output_file}")
