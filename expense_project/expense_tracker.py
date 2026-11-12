import os
import json
import datetime
from expense import Expense




#main function

def main():
    print("Welcome to the Expense Tracker!")
    expense_file_path = os.path.join(os.path.dirname(__file__), "expenses.csv")
    json_file_path = os.path.join(os.path.dirname(__file__), "expenses.json")
    convert_csv_to_json(expense_file_path, json_file_path)

    #Get user input for expense details
    expense = get_user_expense()

    #name = input("Enter expense name: ")
    #category = input("Enter expense category: ")
    #amount = float(input("Enter expense amount: "))

    #Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    #Read file and summarize expenses
    summarize_expenses(expense_file_path)

    
def convert_csv_to_json(expense_file_path, json_file_path):
    expenses = []

    with open(expense_file_path, "r") as f:
        for line in f:
            stripped_line = line.strip()

            if not stripped_line:
                continue

            expense_name, expense_category, expense_amount = stripped_line.split(",")

            expense_data = {
                "name": expense_name,
                "category": expense_category,
                "amount": float(expense_amount)
            }

            expenses.append(expense_data)

    with open(json_file_path, "w") as f:
        json.dump(expenses, f, indent=4)

    print("Expenses successfully converted to JSON!")



def get_user_expense():
    print(f"Getting User Expense")

#Where its getting stored
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    print(f"You entered {expense_name} with amount {expense_amount}")
    expense_categories = [
        "Food",
        "Transport",
        "Home",
        "Entertainment",
        "Miscellaneous"
    ]


#while loop
 
    while True:
        print("Select Category: ")

        for i, category in enumerate(expense_categories):
            print(f"  {i + 1}. {category}")

        value_range = f"1-{len(expense_categories)}"
        selected_index = input(f"Select category by number {value_range}: ")

        if selected_index.isdigit():
            selected_index = int(selected_index) - 1

            if selected_index in range(len(expense_categories)):
                selected_category = expense_categories[selected_index]
                print(f"You selected: {selected_category}")
                break
            else:
                print("Invalid selection. Please try again.")
        else:
            print("Please enter a valid number.")

    return Expense(expense_name, selected_category, expense_amount)


def save_expense_to_file(expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(expense_file_path):
    print(f"Summarizing User Expense")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_category, expense_amount = stripped_line.split(",")
            print(expense_name, expense_amount, expense_category)
            line_expense = Expense(
                name=expense_name, category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else: amount_by_category[key] = expense.amount

    print("Expense Summary by Category:")
    now = datetime.datetime.now()
    day_of_month = now.day
    name_of_month = now.strftime("%B")
    year = now.year
    print(f"Report for {name_of_month} {day_of_month}, {year}")

    for key, value in amount_by_category.items():
        print(f"{key}: Total Amount: ${value:.2f}")

   
if __name__ == "__main__":
    main()
