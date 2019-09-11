import csv

# A function I found for formatting currency (used later)
def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

# Opens the file into a dictionary reader object
with open('budget_data.csv') as budget_data:
    budget_dict = csv.DictReader(budget_data)

    total_months = 0
    total_profit = 0
    this_months_profit = 0
    last_months_profit = 0
    profit_change = 0
    total_change = 0
    top_increase_date = 0
    top_increase_amount = 0
    top_decrease_date = 0
    top_decrease_amount = 0

    # Iterates through every month, counting months and adding up total profit
    for row in budget_dict:
        total_months = total_months + 1
        this_months_profit = (int(row['Profit/Losses']))
        total_profit += this_months_profit

        # For month 2 onward--figures out change in monthly profit
        if total_months > 1:
            profit_change = this_months_profit - last_months_profit
            total_change += profit_change

            # Tests to see if this is a top monthly increase or decrease
            if (profit_change > top_increase_amount): 
                top_increase_amount = profit_change
                top_increase_date = (row['Date'])

            if (profit_change < top_decrease_amount):
                top_decrease_amount = profit_change
                top_decrease_date = (row['Date'])

            # Stores monthly profit for next month's calculations
            last_months_profit = this_months_profit
        
        # For month 1, there is no change calculation; just stores monthly profit for next month
        else:
            last_months_profit = this_months_profit
            continue

    # We've gone through all the months-- print results--
    print(f"Total months: {(total_months)}")
    print(f"Total Profit/Loss : {as_currency(total_profit)}")
    print(f"Average Change: {as_currency((total_change/(total_months-1)))}")
    print(f"Greatest Increase in Profits: {top_increase_date} {as_currency(top_increase_amount)}")
    print(f"Greatest Decrease in Profits: {top_decrease_date} {as_currency(top_decrease_amount)}")

    # Write results to text file
    resultsfile = open("pyBankResults.txt","w") 
 
    print(f"Total months: {(total_months)}", file = resultsfile)
    print(f"Total Profit/Loss : {as_currency(total_profit)}", file = resultsfile)
    print(f"Average Change: {as_currency((total_change/(total_months-1)))}", file = resultsfile)
    print(f"Greatest Increase in Profits: {top_increase_date} {as_currency(top_increase_amount)}", file = resultsfile)
    print(f"Greatest Decrease in Profits: {top_decrease_date} {as_currency(top_decrease_amount)}", file = resultsfile)
    
    resultsfile.close() 
