#!/usr/bin/python3

from expenses import Expenses
from expense import Expense


exp = Expenses()


def menu():
    while True:
        print("---> MENU <---")
        print("1. ADD AN EXPENSE")
        print("2. SAVE TO A FILE")
        print("3. READ FROM A FILE")
        print("4. FIND TOP SPEND CATAGORY")
        print("5. EXIT")
        choice = int(input("ENTER YOUR CHOICE(1-5)"))
        if 0 < choice <= 5:
            return choice


# main function
while True:
    choice = menu()
    print(choice)
    if choice == 1:
        exp.add_expense(Expense(100, 1))
        exp.display()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        exit()
