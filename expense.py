class Expense:
    types = ['Food', 'Travel', 'Books', "Education", 'Movies', 'Rent', 'Entertainment']
    def __init__(self, amount, type):
        self.amount = float(amount)
        self.type = int(type)

    def __str__(self):
        return f'Spent {self.amount} on {Expense.types[self.type]}'

    def get_types():
        return Expense.types