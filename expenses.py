from expense import Expense
import json


class Expenses:
    def __init__(self) -> None:
        self.expenses_list = []

    def add_expense(self, exp):
        self.expenses_list.append(exp.to_dict())

    def display(self):
        for e in self.expenses_list:
            print(str(e))

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.expenses_list, file)

    def get_from_json(self, filename):
        data = []
        self.expenses_list = []
        with open(filename, 'r') as file:
            data = json.load(file)
        for d in data:
            #print(d['amount'], Expense.types.index(d['type']))
            self.add_expense(Expense(d['amount'], Expense.types.index(d['type'])))
