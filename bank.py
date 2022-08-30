class Bank:
    def __init__(self, balance=0.00):
        self.balance = balance

    def log_transaction(self, transaction):
        with open("transaction.txt", "a") as file:
            file.write(f"{transaction} with a new balance of {self.balance}\n")

    def withdraw(self, amount):
        if amount:
            self.balance -= amount
            self.log_transaction(f"withdrawn ${amount}")

    def deposit(self, amount):
        self.balance += amount
        self.log_transaction(f"deposited ${amount}")


account = Bank(100.00)
while True:
    user_action = input("would you like to withdraw(w) or deposit(d)? ")
    if user_action in ["w", "d"]:
        if user_action == "w":
            amount = float(input("how much do you want to withdraw? "))
            account.withdraw(amount)
        elif user_action == "d":
            amount = float(input("how much do you want to deposit? "))
            account.deposit(amount)
    else:
        print("your new balance is", account.balance)

