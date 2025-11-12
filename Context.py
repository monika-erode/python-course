class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Balance {balance} is too low for withdrawal of {amount}")
        self.balance = balance
        self.amount = amount

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    else:
        print("Withdrawal successful!")

try:
    withdraw(1000, 1500)
except InsufficientBalanceError as e:
    print(e)
