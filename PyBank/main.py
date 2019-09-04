import csv
import os

bank.csv = os.path.join( "Resources", "budget_data.csv")


with open(bank.csv, newline="") as csvfile:
    bank = csv.reader(csvfile, delimiter=",")
for row in bank:
    print(bank.csv)

    

    
def print_sum(budget_data):
    months = str(budget_data[0])
    profit = int(budget_data[1])
    losses = int(budget_data[1]) 
        
print(months = bank.csv["Date"].sum())
print(profit = bank.csv["profit"].sum())
print(losses = bank.csv["losses"].sum())
print(profit = bank.csv["profit"].average())
print(max(bank.csv["profit"]))
print(min(bank.csv["losses"])) 


Total_Months = []
Total = []
Average_Change = []
Greatest_Increase_in_Profits =[]
Greatest_Decrease_in_Profits =[]

with open(bank.csv , newline="") as csvfile: bank = csv.reader(csvfile, delimiter=",")
for row in bank:
    Total_Months.append([2])
    Total.append([3])
    Average_Change.append([4])
    Greatest_Increase_in_Profits.append([5])
    Greatest_Decrease_in_Profits.append([6])

print(Total_Months)
print(Total)
print(Average_Change)
print(greatest_Increase_in_Profits)
print(Greatest_Decrease_in_Profits)