#Walkthrough of how to create an Expense Tracker
#https://www.youtube.com/watch?v=HTD86h69PtE

#Creating the Expense class
class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        

 
#representation?
    def __repr__(self) -> str:
        return f"Expense(name={self.name}, category={self.category}, amount={self.amount})"
