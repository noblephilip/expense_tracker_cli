from expense import Expense

class Expenses:
    def __init__(self) -> None:
        self.expenses_list = []
    
    def add_expense(self, exp):
        self.expenses_list.append(exp)
    