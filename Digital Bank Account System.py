class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance


# Creating an object (an instance of the class)
my_account = BankAccount("Aditya", 500)

# Printing the attributes of our object
print("Account Owner:", my_account.owner)
print("Current balance:", my_account.balance)
