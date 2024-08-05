from expense import Expense


class Expenses:
    def __init__(self) -> None:
        self.expenses_list = []

    def add_expense(self, exp):
        self.expenses_list.append(exp)

    def display(self):
        for e in self.expenses_list:
            print(e)
