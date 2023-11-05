#create a program that simulates the all ATM functionalities and operations like checking balance deposit withdrawal using Python functions.

account_balance = 1000

def check_balance():
    print(f"Your account balance is ${account_balance:.2f}")

def deposit():
    global account_balance
    amount = float(input("Enter the amount to deposit: $"))
    if amount > 0:
        account_balance += amount
        print(f"${amount:.2f} has been successfully deposited.")
    else:
        print("Invalid deposit amount.")

def withdraw():
    global account_balance
    amount = float(input("Enter the amount to withdraw: $"))
    if amount > 0:
        if amount <= account_balance:
            account_balance -= amount
            print(f"${amount:.2f} has been successfully withdrawn.")
        else:
            print("Insufficient funds. Your account balance is not enough for this withdrawal.")
    else:
        print("Invalid withdrawal amount.")

def atm():
    while True:
        print("\nATM Simulator")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

atm()
