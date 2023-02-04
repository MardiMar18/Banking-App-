

def show_balance(balance):
    (float(balance))
    print(f"Current Balance: {balance}")

def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    return balance + amount

def withdraw (balance):
    amount = int(input("Enter amount to withdraw: "))
    return balance - amount

def logout (name):
    print (f"Goodbye {name}")