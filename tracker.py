from Proj import Money_Spends
import calendar
import datetime

def main():
    print("Running Expensive Tracker!")
    expense_file_location = "expense_File.csv"
    budget = 2500
    # Get user input for expense
    expense_Details = getting_user_expense()
    # Write expense in a File
    save_expense_in_file(expense_Details,expense_file_location)

    # Read expense File
    summarize(expense_file_location,budget)
    pass 

def getting_user_expense() :
    print("Getting User Expansen")
    Expanse_name = input("Enter Expanse name : ")
    Expanse_amount = float(input("Enter Expanse amount : "))
    print(f"You entered Expanse is {Expanse_name}\nAmount of Expanse is {Expanse_amount}")

    Expanse_category = ["Fun","Home","Food","Work"]
    while True :
        print("Select a category: ")
        for i in range(1,len(Expanse_category)+1) :
            print(f"{i}. {Expanse_category[i-1]}")
        select_category = int(input(f"Enter a category number [1-{len(Expanse_category)}] : "))
        if select_category in range(len(Expanse_category)+1) :
            selected_item = Expanse_category[select_category]
            new_expense = Money_Spends(name=Expanse_name,category=selected_item,amount=Expanse_amount)
            return new_expense
            
        else :
            print("Invalid category!")

def save_expense_in_file(expense_Details : Money_Spends,expense_file_location) :
    print(f"Saving User Expanse: {expense_Details} to {expense_file_location}") 
    with open(expense_file_location, "a") as f:
        f.write(f"{expense_Details.name},{expense_Details.category},{expense_Details.amount}\n")
    
def summarize(expense_file_location,budget) :
    print("Saving User Expanse")
    expenses : list[Money_Spends] = []
    with open(expense_file_location, "r") as f:
        details = f.readlines()
        for li in details :
            expense_name,expense_category,expense_amount = li.strip().split(",")
            line_expense = Money_Spends(expense_name,expense_category,float(expense_amount))
            expenses.append(line_expense)
    amount_by_category = {}
    for expense in expenses :
        key = expense.category
        if key in amount_by_category :
            amount_by_category[key] += expense.amount
        else :
            amount_by_category[key] = expense.amount
    print("Expense by category :")
    for key,amount in amount_by_category.items():
        print(f" {key}: {amount:.2f}INR")
    total_spent = sum([ea.amount for ea in expenses])
    print(f"You are spent {total_spent:.2f}INR this month!")
    remaining_budget = budget-total_spent
    if remaining_budget > 0 :
        print(green(f"Budget Remaining: {remaining_budget:.2f}INR"))
    else :
        print(red(f"Budget Remaining: {remaining_budget:.2f}INR"))

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month-now.day
    daily_budget = remaining_budget/remaining_days
    print(green(f"Budget per Days: {daily_budget:.2f}INR"))
def green(text) :
    return f"\033[92m{text}\033[0m"
def red(text) :
    return f"\033[91m{text}\033[0m"
if __name__ =="__main__" :
    main()
