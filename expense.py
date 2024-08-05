class Expense:
    def __init__(self, amount, type):
        self.amount = amount
        self.type = type

    def __str__(self):
        return f'Spent {self.amount} on {self.type}'
