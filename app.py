from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

"          === Automated Teller Machine ===          "
name = input("Enter Name to Register")
pin = input("Enter PIN: ")

balance = 0
# print (name, balance)
print (f"{name} has been registered with a starting balance of ${balance}.")


"          === Automated Teller Machine ===          "
print("Log In")

while True:
    name_to_validate = input("Please Enter Name")
    pin_to_validate = input("Please Enter Pin Number")

    if name_to_validate == name and pin_to_validate == pin:
        print ("Login successful!")
        break 

    else:
        print ("Invalid credentials!")
        continue 

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    
    if option == "1":
        account.show_balance (balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option =="3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else: 
        print("Invalid Option, please select again.")
