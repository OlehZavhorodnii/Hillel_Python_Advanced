from datetime import datetime


class BankAccount:

    def __init__(self):
        self._log = dict()
        self.balance = 0
        print("Welcome to the Your Balance")

    def withdraw(self):
        amount = float(input("Enter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
            transaction = {f"Withdraw {datetime.now()}": amount}
            self._log_transactions(transaction)
        else:
            print("\n Insufficient balance ")

    def deposit(self):
        amount = float(input("Enter amount to be deposited: "))
        if amount <= 10000:
            self.balance += amount
            print("\n Amount Deposited:", amount)
            transaction = {f"Deposit {datetime.now()}": amount}
            self._log_transactions(transaction)
        else:
            print("\n The amount of accrual should not exceed 10,000")

    def display(self):
        print("\n Net Available Balance =", self.balance)

    def _log_transactions(self, transaction):
        self._log.update(transaction)
        return self._log

    def get_transactions(self):
        print(self._log)


mono = BankAccount()

print("Please select and enter an operation: "
      "\n    Withdraw:               Enter 1; "
      "\n    Deposit:                Enter 2;"
      "\n    Balance on the display: Enter 3; "
      "\n    Get transaction info:   Enter 4;"
      "\n    Exit:                   Enter 0"
      "\nEnter an operation: ")

while True:
    operation = input()
    if operation == "1":
        mono.withdraw()
    elif operation == "2":
        mono.deposit()
    elif operation == "3":
        mono.display()
    elif operation == "4":
        mono.get_transactions()
    elif operation == "0":
        exit()
    else:
        print("Please enter correct data")
