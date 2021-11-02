import logging
import os


class BankAccount:

    def __init__(self):
        self.__log = 0
        self.__transaction = ''
        self.__balance = 0

    def withdraw(self, amount_withdraw):
        if self.__balance >= amount:
            self.__balance -= amount
            self.__transaction = f"Withdraw {amount}"
            self._log_transactions(self.__transaction)
            return amount_withdraw

    def deposit(self, amount_deposit):
        if amount <= 10000:
            self.__balance += amount
            self.__transaction = f"Deposit {amount}"
            self._log_transactions(self.__transaction)
            return amount_deposit

    def display(self):
        return self.__balance

    def _log_transactions(self, __transaction):
        self.__log += 1
        if self.__log > 0:
            logging.basicConfig(filename='BankAccount.log', filemode='w', format='%(asctime)s - %(message)s',
                                datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
        return logging.info(str(self.__transaction))

    def get_transactions(self):
        if os.path.isfile('BankAccount.log'):
            log = open('BankAccount.log', 'r')
            return log.read()


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
        amount = float(input("Enter amount to be withdrawn: "))
        if mono.withdraw(amount):
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance ")
    elif operation == "2":
        amount = float(input("Enter amount to be deposited: "))
        if mono.deposit(amount):
            print("\n Amount Deposited:", amount)
        else:
            print("\n The amount of accrual should not exceed 10,000")
    elif operation == "3":
        print("\n Net Available Balance = " + str(mono.display()))
    elif operation == "4":
        if mono.get_transactions():
            print(str(mono.get_transactions()))
        else:
            print('No transactions')
    elif operation == "0":
        exit()
    else:
        print("Please enter correct data")
