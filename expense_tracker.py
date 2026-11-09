from expense import Expense



#main function

def main():
    print("Welcome to the Expense Tracker!")
    expense_file_path = "expenses.csv"

    #Get user input for expense details
    expense = get_user_expense()

    #name = input("Enter expense name: ")
    #category = input("Enter expense category: ")
    #amount = float(input("Enter expense amount: "))

    #Write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    #Read file and summarize expenses
    summarize_expenses(expense_file_path)
   



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
    return Expense(expense_name, selected_category, expense_amount) 

def save_expense_to_file(expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def summarize_expenses(expense_file_path):
    print(f"Summarizing User Expense from {expense_file_path}")

if __name__ == "__main__":
    main()
  